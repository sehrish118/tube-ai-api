import chromadb  # using chromadb python package


class ChromaVectorStore:
    def __init__(
        self,
        path: str = "./chroma_db",  # current working directory of our project(this will be our local vector db)
        collection_name: str = "youtube_transcripts",
    ):
        self.client = chromadb.PersistentClient(
            path=path
        )  # chromadb data will be persistent on disk
        # so if program stops -> Data will remain

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )  # if collection exist use it, otherwise create it

    # def add_chunk(
    #     self, chunk_id: str, text: str, embedding: list[float], metadata: dict
    # ) -> None:
    #     self.collection.add(
    #         ids=[chunk_id],
    #         documents=[text],
    #         embeddings=[embedding],
    #         metadatas=[metadata],
    #     )

    def add_chunk(
        self,
        chunk_id: str,
        text: str,
        embedding: list[float],
        metadata: dict,
    ) -> None:

        print("\n===== CHROMA ADD =====")
        print("Chunk ID:", chunk_id)
        print("Metadata:", metadata)
        print("Embedding length:", len(embedding))
        print("DB path:", self.client)
        print("======================")

        self.collection.add(
            ids=[chunk_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata],
        )

        print(
            "Successfully added.",
            "Collection count:",
            self.collection.count(),
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 5,
        video_id: str | None = None,
    ):
        query = {
            "query_embeddings": [query_embedding],
            "n_results": top_k,
        }
        if video_id:
            query["where"] = {"video_id": video_id}
        print("\n===== VECTOR STORE SEARCH =====")
        print("video_id:", repr(video_id))
        print("query:", query)
        print("collection count:", self.collection.count())
        print("===============================\n")
        return self.collection.query(**query)
