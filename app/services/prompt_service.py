from app.models.prompt import RAGPrompt


class PromptService:
    def build_prompt(
        self,
        question: str,
        context: str,
    ) -> RAGPrompt:

        system_prompt = """
You are a helpful AI assistant that answers questions
about YouTube videos.

Use the provided context to answer the user's question.

Do not use information that is not supported by the context.

If the answer cannot be found in the context,
say that the information is not available in the video.
""".strip()

        user_prompt = f"""
--- BEGIN CONTEXT ---

{context}

--- END CONTEXT ---

--- QUESTION ---

{question}

--- END QUESTION ---
""".strip()

        return RAGPrompt(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )
