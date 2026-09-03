from fastapi import APIRouter

from app.schemas.rag import AskRequest, AskResponse
from app.services.rag_service import RAGService


router = APIRouter(prefix="/rag", tags=["RAG"])

rag_service = RAGService()


@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    answer = await rag_service.answer(
        question=request.question,
        video_id=request.video_id,
    )

    return AskResponse(
        video_id=request.video_id,
        question=request.question,
        answer=answer,
    )
