from enum import Enum
from typing import Optional


class KernelException(Exception):
    class ErrorCodes(Enum):
        UnknownError = -1
        InvalidFunctionDescription = 0
        FunctionOverloadNotSupported = 1
        FunctionNotAvailable = 2
        FunctionTypeNotSupported = 3
        InvalidFunctionType = 4
        InvalidBackendConfiguration = 5
        BackendNotFound = 6
        SkillCollectionNotSet = 7
        AmbiguousImplementation = 8

    _error_code: ErrorCodes

    def __init__(
        self,
        error_code: ErrorCodes,
        message: str,
        inner_exception: Optional[Exception] = None,
    ) -> None:
        """Initializes a new instance of the KernelError class.

        Arguments:
            error_code {ErrorCodes} -- The error code.
            message {str} -- The error message.
            inner_exception {Exception} -- The inner exception.
        """
        super().__init__(error_code, message, inner_exception)
        self._error_code = error_code

    @property
    def error_code(self) -> ErrorCodes:
        """Gets the error code.

        Returns:
            ErrorCodes -- The error code.
        """
        return self._error_code