from fastapi import APIRouter
from app.schemas import InferenceRequest

router = APIRouter()

@router.get("/")
def root():
    return {"service": "ai-eval-service", "status": "ok"}

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/inference")
def inference(request: InferenceRequest):
    return {
        "message": "Inference endpoint stub",
        "received_prompt": request.prompt
    }