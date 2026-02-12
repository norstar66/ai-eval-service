from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="AI Evaluation & Inference Service", version="1.0.0")

app.include_router(router)

#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)