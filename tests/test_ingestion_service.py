from app.services.ingestion_service import IngestionService


service = IngestionService()

result = service.ingest_video("RSEOYH_OpRc")

print(result)
