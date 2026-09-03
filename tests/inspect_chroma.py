from app.integrations.vector_store import ChromaVectorStore


store = ChromaVectorStore()

print("\n===== CHROMA DEBUG =====")

print("Collection name:")
print(store.collection.name)

print("Total documents:")
print(store.collection.count())

data = store.collection.get(
    include=["documents", "metadatas"]
)

print("\nIDs:")
print(data["ids"])

print("\nMetadata:")
for metadata in data["metadatas"]:
    print(metadata)

print("========================\n")