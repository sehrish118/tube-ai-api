from dataclasses import dataclass


@dataclass
class RAGPrompt:
    system_prompt: str
    user_prompt: str
