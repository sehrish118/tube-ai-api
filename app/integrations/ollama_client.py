import httpx


class OllamaClient:
    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        # Pass timeout=None to allow long local model generation without Timing Out
        timeout: float | None = None,
    ):
        self.base_url = base_url
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=timeout,  # Disables timeout by default
        )

    async def chat(
        self,
        model: str,
        messages: list[dict[str, str]],
    ) -> str:
        response = await self.client.post(
            "/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": False,
            },
        )

        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]

    async def close(self):
        """Clean up the underlying httpx client connection pool."""
        await self.client.aclose()
