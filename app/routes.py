from fastapi import APIRouter
from app.schemas import InferenceRequest
from app.logger import log_inference


router = APIRouter()

@router.get("/")
def root():
    return {"service": "ai-eval-service", "status": "ok"}

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/inference")
def inference(request: InferenceRequest):
    llm_response = ""
    metrics = {}
    evaluation = {}
    log_inference({
        "prompt": request.prompt,
        "response": llm_response,
        "metrics": metrics,
        "evaluation": evaluation,
    })
    return {
        "message": "Inference endpoint stub",
        "received_prompt": request.prompt
    }