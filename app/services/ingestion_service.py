# from app.services.chunk_service import ChunkService
# from app.services.embedding_service import EmbeddingService
# from app.integrations.vector_store import ChromaVectorStore
# from app.schemas.transcript import VideoTranscript


# class IngestionService:
#     def __init__(self):
#         self.chunk_service = ChunkService()
#         self.embedding_service = EmbeddingService()
#         self.vector_store = ChromaVectorStore()

#     def ingest(self, transcript: VideoTranscript) -> int:

#         chunks = self.chunk_service.create_chunks(transcript)

#         for chunk in chunks:
#             embedding = self.embedding_service.embed_chunk(chunk)

#             metadata = {
#                 "video_id": chunk.video_id,
#                 "chunk_index": chunk.chunk_index,
#                 "start_time": chunk.start_time,
#                 "end_time": chunk.end_time,
#             }

#             self.vector_store.add_chunk(
#                 chunk_id=chunk.chunk_id,
#                 text=chunk.text,
#                 embedding=embedding,
#                 metadata=metadata,
#             )

#         return len(chunks)


from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.integrations.vector_store import ChromaVectorStore
from app.schemas.transcript import VideoTranscript


class IngestionService:
    def __init__(self):
        self.chunk_service = ChunkService()
        self.embedding_service = EmbeddingService()
        self.vector_store = ChromaVectorStore()

    def ingest(self, transcript: VideoTranscript) -> int:

        print("\n===== INGESTION START =====")
        print("Video ID:", repr(transcript.video_id))
        print("Number of transcript segments:", len(transcript.segments))

        chunks = self.chunk_service.create_chunks(transcript)

        print("Number of chunks:", len(chunks))

        for i, chunk in enumerate(chunks):
            print(f"\n--- Processing chunk {i} ---")
            print("Chunk ID:", chunk.chunk_id)
            print("Chunk video ID:", repr(chunk.video_id))
            print("Text length:", len(chunk.text))

            embedding = self.embedding_service.embed_chunk(chunk)

            print("Embedding generated:", len(embedding))

            metadata = {
                "video_id": chunk.video_id,
                "chunk_index": chunk.chunk_index,
                "start_time": chunk.start_time,
                "end_time": chunk.end_time,
            }

            print("Metadata:", metadata)

            self.vector_store.add_chunk(
                chunk_id=chunk.chunk_id,
                text=chunk.text,
                embedding=embedding,
                metadata=metadata,
            )

            print("ChromaDB count after add:", self.vector_store.collection.count())

        print("\n===== INGESTION COMPLETE =====")
        print("Total chunks ingested:", len(chunks))
        print("===============================\n")

        return len(chunks)
