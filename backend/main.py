"""FastAPI application for PowerFit Fitness Coach.
Serves the ChatKit endpoint for the web interface.
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, StreamingResponse

from server import server

# Load environment variables
load_dotenv()

# Verify OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is required")

# Create FastAPI app
app = FastAPI(
    title="PowerFit Fitness Coach API",
    description="AI fitness coaching assistant with ChatKit integration",
    version="1.0.0"
)

# Configure CORS for ChatKit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "service": "PowerFit Fitness Coach",
        "status": "running",
        "version": "1.0.0",
        "chatkit_endpoint": "/chatkit"
    }


@app.get("/health")
async def health():
    """Detailed health check."""
    return {
        "status": "healthy",
        "store": "in-memory",
        "openai_api_key_set": bool(os.getenv("OPENAI_API_KEY"))
    }


@app.post("/chatkit")
async def chatkit_endpoint(request: Request):
    """ChatKit protocol endpoint."""
    payload = await request.body()
    result = await server.process(payload, {"request": request})

    if hasattr(result, '__aiter__'):
        # Streaming response
        return StreamingResponse(
            result,
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            }
        )
    else:
        # JSON response
        return Response(
            content=result.json if hasattr(result, 'json') else result,
            media_type="application/json"
        )


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
    )
