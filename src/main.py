from fastapi import FastAPI, Depends, HTTPException, UploadFile
from src.upload import Upload
import uvicorn
from src.user import User

app = FastAPI()
db_entity = User(host="localhost", user="your_user", password="your_password", database="your_database")

@app.get("/")
def welcome():
    return {"message": "Welcome to SmartDocAssistant - Your document-based AI assistant!"}

@app.post("/upload-file/")
async def upload_file(file: UploadFile):
    """Upload a document for processing."""
    try:
        response = Upload.uploadDocument(file)
        return {"status": "success", "data": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/register/")
async def create_user(user_request: dict):
    """Register a new user."""
    try:
        user = db_entity.create_user(
            username=user_request['username'],
            email=user_request['email_id'],
            password=user_request['password']
        )
        return {"status": "success", "user_id": user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login/")
async def login(credentials: dict):
    """Log in an existing user."""
    try:
        username = credentials['username']
        password = credentials['password']
        user = db_entity.get_user(username, password)
        if user:
            user_id, _, _ = user
            return {"status": "success", "user_id": user_id}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

