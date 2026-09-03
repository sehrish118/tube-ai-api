from app.models.retrieval import RetrievedChunk


class ContextService:
    # def build_context(self,chunks:list[RetrievedChunk])->str:
    #     context_parts = []

    #     for i, chunk in enumerate(chunks,start=1):
    #         context_parts.append(
    #             f"[Source {i}]\n"
    #             f"{chunk.text}"
    #         )

    #     return "\n\n".join(context_parts)

    def build_context(self, chunks: list[RetrievedChunk]) -> str:
        context_parts = []

        for i, chunk in enumerate(chunks, start=1):
            metadata = chunk.metadata

            source = (
                f"[Source {i}]\n"
                f"Video ID: {metadata.get('video_id')}\n"
                f"Timestamp: "
                f"{metadata.get('start_time')} - "
                f"{metadata.get('end_time')}\n"
                f"Text: {chunk.text}"
            )
            context_parts.append(source)

        return "\n\n".join(context_parts)
