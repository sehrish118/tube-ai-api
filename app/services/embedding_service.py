from app.integrations.embedding_client import EmbeddingClient
from app.schemas.chunk import TextChunk


class EmbeddingService:
    def __init__(self):
        self.client = EmbeddingClient()

    def embed_text(self, text: str) -> list[float]:
        return self.client.embed(text)

    def embed_chunk(self, chunk: TextChunk) -> list[float]:
        return self.client.embed(chunk.text)
