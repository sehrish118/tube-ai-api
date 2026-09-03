# 🎥 Tube AI API

A backend API that allows users to ask questions about YouTube videos without watching the entire video.

Tube AI API uses **Retrieval-Augmented Generation (RAG)** to convert YouTube video content into searchable knowledge and generate answers from the most relevant parts of the video.

---

## 🚀 Project Overview

The basic idea is simple:

> Give the API a YouTube video, then ask questions about that video.

The system:

1. Extracts the YouTube video ID
2. Retrieves the video's transcript
3. Uses Whisper as a fallback when a transcript is unavailable
4. Splits the transcript into smaller chunks
5. Generates embeddings for each chunk
6. Stores the embeddings in ChromaDB
7. Performs semantic search when a question is asked
8. Retrieves the most relevant chunks
9. Builds a context-aware prompt
10. Sends the prompt to Llama 3.2 through Ollama
11. Returns the generated answer

---

## 🏗️ Architecture

```text
                    YouTube Video
                          │
                          ▼
                  Video Processing
                          │
                          ▼
                ┌───────────────────┐
                │ Transcript Source │
                └───────────────────┘
                    │           │
             Available        Unavailable
                    │           │
                    ▼           ▼
              YouTube API     yt-dlp
                                │
                                ▼
                              Audio
                                │
                                ▼
                             Whisper
                                │
                    ┌───────────┘
                    ▼
              VideoTranscript
                    │
                    ▼
               ChunkService
                    │
                    ▼
            EmbeddingService
                    │
                    ▼
                ChromaDB
                    │
                    │
        ────────────┴────────────
                    │
                User Question
                    │
                    ▼
            Query Embedding
                    │
                    ▼
             Semantic Search
                    │
                    ▼
            Relevant Chunks
                    │
                    ▼
                 Context
                    │
                    ▼
                 Prompt
                    │
                    ▼
               Llama 3.2
                 Ollama
                    │
                    ▼
                  Answer



🧠 RAG Pipeline

The project follows a Retrieval-Augmented Generation architecture.

1. Retrieval

The user's question is converted into an embedding.

The embedding is used to search ChromaDB for semantically similar transcript chunks.

2. Augmentation

The retrieved chunks are combined to create the context for the language model.

3. Generation

The context and user's question are sent to Llama 3.2 through Ollama.

The model generates the final answer using the retrieved video content.

Question
   ↓
Embedding
   ↓
Semantic Search
   ↓
Relevant Chunks
   ↓
Context
   ↓
Prompt
   ↓
Llama 3.2
   ↓
Answer
🎙️ Automatic Whisper Fallback

Not every YouTube video has an accessible transcript.

Tube AI API handles this situation automatically.

Normal case
YouTube Video
     ↓
YouTube Transcript API
     ↓
Transcript
Fallback case
YouTube Video
     ↓
Transcript unavailable
     ↓
yt-dlp
     ↓
Audio
     ↓
faster-whisper
     ↓
Generated Transcript

Both approaches produce the same internal VideoTranscript structure, so the rest of the RAG pipeline does not need to know where the transcript came from.

🛠️ Tech Stack
Technology	Purpose
Python	Backend programming
FastAPI	REST API framework
YouTube Transcript API	Transcript extraction
yt-dlp	YouTube audio downloading
faster-whisper	Local speech-to-text fallback
Ollama	Local AI model runtime
Llama 3.2	Text generation
nomic-embed-text	Text embeddings
ChromaDB	Vector database
Pydantic	Data validation
📁 Project Structure
tube_ai_api/
│
├── app/
│   ├── integrations/
│   │   ├── youtube_client.py
│   │   ├── youtube_audio.py
│   │   ├── whisper_client.py
│   │   ├── embedding_client.py
│   │   └── vector_store.py
│   │
│   ├── services/
│   │   ├── video_service.py
│   │   ├── transcript_service.py
│   │   ├── whisper_transcript_provider.py
│   │   ├── chunk_service.py
│   │   ├── embedding_service.py
│   │   ├── ingestion_service.py
│   │   ├── retrieval_service.py
│   │   ├── context_service.py
│   │   ├── prompt_service.py
│   │   └── rag_service.py
│   │
│   ├── schemas/
│   │
│   ├── routers/
│   │
│   ├── exceptions/
│   │
│   └── utils/
│
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md
⚙️ Requirements

Before running the project, make sure you have:

Python 3.9+
Ollama
Llama 3.2 model
nomic-embed-text model

Install the Python dependencies:

pip install -r requirements.txt
🤖 Ollama Models

The project uses Ollama for local AI inference.

Generation model
ollama pull llama3.2
Embedding model
ollama pull nomic-embed-text

Check installed models:

ollama list
▶️ Running the API

Activate the virtual environment:

Windows
.\venv\Scripts\Activate.ps1

Start the FastAPI application:

uvicorn app.main:app --reload

The API will be available locally.

FastAPI's interactive documentation can be accessed through:

/docs
📡 API
Process a YouTube Video
POST /videos/process

Example request:

{
  "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}

Example response:

{
  "video_id": "VIDEO_ID",
  "status": "processed",
  "chunks_created": 10
}

The processing pipeline performs:

YouTube URL
    ↓
Video ID extraction
    ↓
Transcript extraction
    ↓
Whisper fallback if necessary
    ↓
Chunking
    ↓
Embedding
    ↓
ChromaDB
🔍 Semantic Retrieval

When a user asks a question:

Question
   ↓
Question Embedding
   ↓
ChromaDB
   ↓
Similarity Search
   ↓
Top-K Relevant Chunks

The system also supports filtering retrieved chunks by video_id, ensuring that questions can be answered using content from the requested video.

🧪 Testing

The project contains individual tests for important integrations and services.

Examples:

python -m tests.test_ollama_client
python -m tests.test_ytdlp
python -m tests.test_whisper
python -m tests.test_whisper_provider

Tests are kept inside the repository to make the development process reproducible and easier to maintain.

🔐 Environment & Local Data

Sensitive environment variables should be stored in .env.

The following are intentionally excluded from Git:

.env
venv/
chroma_db/
__pycache__/
*.pyc
temporary audio/video files

These files and directories are local development artifacts and should not be committed to the repository.

🎯 Current Features
 YouTube URL processing
 YouTube video ID extraction
 YouTube transcript extraction
 Automatic Whisper fallback
 YouTube audio downloading
 Transcript chunking
 Text embeddings
 ChromaDB vector storage
 Video-specific semantic retrieval
 RAG pipeline
 Ollama integration
 Llama 3.2 integration
 FastAPI REST API
 Component-level testing
🚧 Future Improvements
Better transcript exception handling
Retry mechanism for temporary failures
Improved temporary-file cleanup
Whisper model lifecycle optimization
Duplicate video/chunk prevention
Transcript source metadata
Better API error responses
More comprehensive automated tests
Improved chunking strategies
Authentication and rate limiting
Production deployment
📚 What I Learned

This project is being built to understand how a real backend AI application works internally.

Key concepts explored:

REST API architecture
FastAPI
Dependency injection
Service-layer architecture
Data validation with Pydantic
YouTube transcript extraction
Speech-to-text
Text chunking
Embeddings
Vector databases
Semantic search
Retrieval-Augmented Generation
Local LLM inference
API integration
Error handling
Backend testing
📌 Project Status

🚧 Currently under active development

The core YouTube → RAG pipeline is functional, with automatic Whisper transcription fallback for videos without accessible transcripts.

More production-level improvements will be added incrementally.

👩‍💻 Author

Built as a hands-on project to understand backend development and AI/RAG systems by implementing the architecture step by step.


### Ek important point

README mein maine **sirf woh features `Current Features` mein rakhe hain jo humne actually implement/test kiye hain**. Jo cheezein abhi baaki hain—jaise duplicate prevention aur refined retry handling—unhein `Future Improvements` mein rakha hai. Ye GitHub README ko honest rakhta hai.

Ab **`.gitignore` + `README.md` dono ready hain**. Next hum `git status` se peh