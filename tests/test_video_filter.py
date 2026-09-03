from app.integrations.vector_store import ChromaVectorStore


store = ChromaVectorStore()

for video_id in [
    "RSEOYH_OpRc",
    "3ieUKDjdLfs",
    "oRcLYB8vaf4",
]:
    result = store.collection.get(
        where={"video_id": video_id},
        include=["documents", "metadatas"],
    )

    print("\n==============================")
    print("VIDEO ID:", video_id)
    print("NUMBER OF CHUNKS:", len(result["ids"]))
    print("IDS:", result["ids"])
    print("METADATA:", result["metadatas"])
    print("==============================")
