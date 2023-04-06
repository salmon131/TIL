from abc import ABC

from semantic_kernel.ai.embeddings.embedding_index_base import EmbeddingIndexBase
class DataStoreBase:
    pass


class MemoryStoreBase(DataStoreBase, EmbeddingIndexBase, ABC):
    pass