from fastapi import Request, status
from fastapi.responses import JSONResponse


from app.exceptions.video import InvalidYoutubeURL
from app.exceptions.transcript import (TranscriptNotAvailable, TranscriptFetchError)

async def invalid_youtube_url_handler(request: Request, exc: Exception) -> JSONResponse:
    if isinstance(exc, InvalidYoutubeURL):
        message = exc.message
    else:
        message = "An unexpected Error occurred."
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": "INVALID_YOUTUBE_URL", "message": message},
    )


async def transcript_not_available_handler(request:Request,exc:Exception)->JSONResponse:
    if isinstance(exc,TranscriptNotAvailable):
        message = exc.message
    else:
        message = "An unexpected error occurred"

    return JSONResponse(
        status_code = status.HTTP_400_NOT_FOUND,
        content = {
            "error": "TRANSCRIPT_NOT_AVAILABLE",
            "message":message
        }
    )

async def transcript_fetch_error_handler(request:Request,exc:Exception)->JSONResponse:
    if isinstance(exc,TranscriptFetchError):
        message = exc.message
    else:
        message = "An unexpected error occurred"

    return JSONResponse(
        status_code = status.HTTP_502_BAD_GATEWAY,
        content = {
            "error":"TRANSCRIPT_FETCH_ERROR",
            "message":message
        }
    )