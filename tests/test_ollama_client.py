import asyncio

from app.integrations.ollama_client import OllamaClient


async def main():

    client = OllamaClient()

    answer = await client.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": "What is RAG? Explain in one sentence.",
            }
        ],
    )

    print(answer)


asyncio.run(main())
