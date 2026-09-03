# from fastapi import FastAPI

# from app.core.config import settings
# from app.routers.health import router as health_router
# from app.routers.videos import router as video_router
# from app.exceptions.video import InvalidYoutubeURL
# from app.exceptions.handlers import invalid_youtube_url_handler,transcript_fetch_error_handler,transcript_not_available_handler
# from app.exceptions.transcript import TranscriptFetchError,TranscriptNotAvailable

# app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

# app.add_exception_handler(InvalidYoutubeURL, invalid_youtube_url_handler)
# app.add_exception_handler(TranscriptNotAvailable, transcript_not_available_handler)
# app.add_exception_handler(TranscriptFetchError,transcript_fetch_error_handler )
# app.include_router(health_router)
# app.include_router(video_router)

from fastapi import FastAPI

from app.routers.rag import router as rag_router
from app.routers.videos import router as video_router

app = FastAPI(
    title="Tube AI API",
)
app.include_router(video_router)
app.include_router(rag_router)
