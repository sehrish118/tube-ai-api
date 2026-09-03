from app.schemas.chunk import TextChunk
from app.schemas.transcript import VideoTranscript


class ChunkService:
    def create_chunks(self,transcript:VideoTranscript,max_character:int=2000,)->list[TextChunk]:
        chunks = []
        current_segments = []
        current_length = 0

        for segment in transcript.segments:
            segment_length = len(segment.text)

            if(current_segments and current_length + segment_length > max_character):
                chunks.append(self.build_chunk(
                    transcript.video_id,
                    current_segments,
                    len(chunks),
                ))

                current_segments = []
                current_length = 0

            current_segments.append(segment)
            current_length += segment_length

        if current_segments:
            chunks.append(
                self.build_chunk(
                    transcript.video_id,
                    current_segments,
                    len(chunks),
                )
            )

        return chunks



    def build_chunk(self,video_id:str,segments,chunk_index:int,)->TextChunk:
        text = " ".join(segment.text for segment in segments)

        return TextChunk(
            chunk_id = f"{video_id}-{chunk_index}",
            video_id = video_id,
            text=text,
            start_time = segments[0].start,
            end_time = (
                segments[-1].start + segments[-1].duration
            ),
            chunk_index = chunk_index,
        )