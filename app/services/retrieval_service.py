from app.integrations.vector_store import ChromaVectorStore
from app.services.embedding_service import EmbeddingService
from app.models.retrieval import RetrievedChunk


class RetrievalService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = ChromaVectorStore()

    # def retrieve(self,question:str,video_id:str|None=None,top_k=5,):
    #     query_embeddings = self.embedding_service.embed_text(question)

    #     return self.vector_store.search(
    #         query_embedding = query_embeddings,
    #         top_k = top_k,
    #         video_id=video_id,
    #     )

    def retrieve(
        self,
        question: str,
        video_id: str | None = None,
        top_k: int = 5,
    ) -> list[RetrievedChunk]:

        query_embedding = self.embedding_service.embed_text(question)

        result = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
            video_id=video_id,
        )

        print("\n===== RETRIEVAL DEBUG =====")
        print("Question:", repr(question))
        print("Video ID:", repr(video_id))
        print("Top K:", repr(top_k))

        print("===========================\n")

        documents = result.get("documents")
        metadatas = result.get("metadatas")
        distances = result.get("distances")
        ids = result.get("ids")

        if not documents or not metadatas or not distances or not ids:
            return []

        chunks = []

        for i, chunk_id in enumerate(ids[0]):
            chunks.append(
                RetrievedChunk(
                    chunk_id=chunk_id,
                    text=documents[0][i],
                    metadata=metadatas[0][i],
                    distance=distances[0][i],
                )
            )

        return chunks
