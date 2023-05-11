from typing import Protocol

from semantic_kernel.kernel_base import KernelBase


class ExtendsKernel(Protocol):
    def kernel(self) -> KernelBase:
        ...