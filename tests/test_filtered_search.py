from app.integrations.vector_store import ChromaVectorStore
from app.services.embedding_service import EmbeddingService


store = ChromaVectorStore()
embedding_service = EmbeddingService()

question = "What is this video about?"
video_id = "RSEOYH_OpRc"

query_embedding = embedding_service.embed_text(question)

result = store.collection.query(
    query_embeddings=[query_embedding],
    n_results=5,
    where={"video_id": video_id},
)

print("\n===== FILTERED SEMANTIC SEARCH =====")

print("Question:")
print(question)

print("\nVideo ID:")
print(video_id)

print("\nIDs:")
print(result["ids"])

print("\nDocuments:")
print(result["documents"])

print("\nMetadatas:")
print(result["metadatas"])

print("\nDistances:")
print(result["distances"])

print("\n====================================")
