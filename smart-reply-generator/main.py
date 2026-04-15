from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from model import IntentClassifier
import os

app = FastAPI(title="Smart Reply API")

# Initialize our model
classifier = IntentClassifier()

# Define Request model
class MessageRequest(BaseModel):
    message: str

# API Endpoint to generate replies
@app.post("/api/generate-replies")
async def generate_replies(request: MessageRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    intent, confidence = classifier.detect_intent(request.message)
    replies = classifier.get_replies(intent)
    
    return {
        "intent": intent.replace("_", " ").title(),
        "confidence": confidence,
        "replies": replies
    }

# Serve Frontend static files
# Ensure 'frontend' directory exists before mounting
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
if not os.path.exists(frontend_dir):
    os.makedirs(frontend_dir)

app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
