from app.integrations.ollama_client import OllamaClient
from app.models.prompt import RAGPrompt


class LLMService:
    def __init__(self):
        self.client = OllamaClient()
        self.model = "llama3.2"

    async def generate(
        self,
        prompt: RAGPrompt,
    ) -> str:
        messages = [
            {
                "role": "system",
                "content": prompt.system_prompt,
            },
            {
                "role": "user",
                "content": prompt.user_prompt,
            },
        ]

        return await self.client.chat(
            model=self.model,
            messages=messages,
        )
