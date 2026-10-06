from fastapi import FastAPI

app = FastAPI(
    title="AI Business Assistant API",
    description="AI-powered business assistant built with FastAPI.",
    version="0.1.0"
)

@app.get("/")
async def root():
    return{
        "project": "AI Business Assistant",
        "status": "running",
        "version": "0.1.0",
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
    }