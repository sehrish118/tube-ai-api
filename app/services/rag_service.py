from app.services.retrieval_service import RetrievalService
from app.services.context_service import ContextService
from app.services.prompt_service import PromptService
from app.services.llm_service import LLMService


class RAGService:
    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.context_service = ContextService()
        self.prompt_service = PromptService()
        self.llm_service = LLMService()

    async def answer(
        self,
        question: str,
        video_id: str,
        top_k: int = 5,
    ) -> str:
        chunks = self.retrieval_service.retrieve(
            question=question,
            video_id=video_id,
            top_k=top_k,
        )

        context = self.context_service.build_context(chunks)

        prompt = self.prompt_service.build_prompt(
            question=question,
            context=context,
        )

        answer = await self.llm_service.generate(prompt)

        return answer
