import os
import sys

from promptlayer.promptlayer import PromptLayerBase

os.environ['PROMPTLAYER_API_KEY'] = 'pl_a9370defcc7ed746045cb7d6b66f1f6e'
api_key = os.environ.get('PROMPTLAYER_API_KEY')

openai = None
try:
    import openai as openai_module

    openai = PromptLayerBase(openai_module, function_name="openai")
except ImportError:
    print(
        "OpenAI module not found. Install with `pip install openai`.", file=sys.stderr
    )
    pass

__all__ = ["api_key", "openai"]