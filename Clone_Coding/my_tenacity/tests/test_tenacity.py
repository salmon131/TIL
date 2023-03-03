import datetime
import logging
import re
import sys
import time
import typing
import unittest
import warnings
from contextlib import contextmanager
from copy import copy
from fractions import Fraction

import pytest
import tenacity
from tenacity import RetryCallState, RetryError, Retrying, retry

_unset = object()


def _make_unset_exception(func_name, **kwargs):
    missing = []
    for k, v in kwargs.items():
        if v is _unset:
            missing.append(k)
    missing_str = ", ".join(repr(s) for s in missing)
    return TypeError(func_name + " func missing parameters: " + missing_str)


def _set_delay_since_start(retry_state, delay):
    # Ensure outcome_timestamp - start_time is *exactly* equal to the delay to
    # avoid complexity in test code.
    retry_state.start_time = Fraction(retry_state.start_time)
    retry_state.outcome_timestamp = retry_state.start_time + Fraction(delay)
    assert retry_state.seconds_since_start == delay


def make_retry_state(
    previous_attempt_number, delay_since_first_attempt, last_result=None
):
    """Construct RetryCallState for given attempt number & delay.

    Only used in testing and thus is extra careful about timestamp arithmetics.
    """
    required_parameter_unset = (
        previous_attempt_number is _unset or delay_since_first_attempt is _unset
    )
    if required_parameter_unset:
        raise _make_unset_exception(
            "wait/stop",
            previous_attempt_number=previous_attempt_number,
            delay_since_first_attempt=delay_since_first_attempt,
        )

    retry_state = RetryCallState(None, None, (), {})
    retry_state.attempt_number = previous_attempt_number
    if last_result is not None:
        retry_state.outcome = last_result
    else:
        retry_state.set_result(None)
    _set_delay_since_start(retry_state, delay_since_first_attempt)
    return retry_state


class TestBase(unittest.TestCase):
    def test_retrying_repr(self):
        class ConcreteRetrying(tenacity.BaseRetrying):
            def __call__(self, fn, *args, **kwargs):
                pass

        repr(ConcreteRetrying())

    def test_callstate_repr(self):
        rs = RetryCallState(None, None, (), {})
        rs.idle_for = 1.1111111
        assert repr(rs).endswith("attempt #1; slept for 1.11; last result: none yet>")
        rs = make_retry_state(2, 5)
        assert repr(rs).endswith(
            "attempt #2; slept for 0.0; last result: returned None>"
        )
        rs = make_retry_state(
            0, 0, last_result=tenacity.Future.construct(1, ValueError("aaa"), True)
        )
        assert repr(rs).endswith(
            "attempt #0; slept for 0.0; last result: failed (ValueError aaa)>"
        )


class TestConditions(unittest.TestCase):
    def test_never_stop(self):
        r = Retrying()
        self.assertFalse(r.stop(make_retry_state(3, 6546)))

    def test_stop_any(self):
        stop = tenacity.stop_any(
            tenacity.stop_after_delay(1), tenacity.stop_after_attempt(4)
        )

        def s(*args):
            return stop(make_retry_state(*args))

        self.assertFalse(s(1, 0.1))
        self.assertFalse(s(2, 0.2))
        self.assertFalse(s(2, 0.8))
        self.assertTrue(s(4, 0.8))
        self.assertTrue(s(3, 1.8))
        self.assertTrue(s(4, 1.8))

    def test_stop_or(self):
        stop = tenacity.stop_after_delay(1) | tenacity.stop_after_attempt(4)

        def s(*args):
            return stop(make_retry_state(*args))

        self.assertFalse(s(1, 0.1))
        self.assertFalse(s(2, 0.2))
        self.assertFalse(s(2, 0.8))
        self.assertTrue(s(4, 0.8))
        self.assertTrue(s(3, 1.8))
        self.assertTrue(s(4, 1.8))

    def test_stop_after_delay(self):
        for delay in (1, datetime.timedelta(seconds=1)):
            with self.subTest(msg=f"{type(delay)}"):
                r = Retrying(stop=tenacity.stop_after_delay(delay))
                self.assertFalse(r.stop(make_retry_state(2, 0.999)))
                self.assertTrue(r.stop(make_retry_state(2, 1)))
                self.assertTrue(r.stop(make_retry_state(2, 1.001)))
