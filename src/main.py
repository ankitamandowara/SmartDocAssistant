from fastapi import FastAPI, HTTPException, UploadFile
from upload import Upload
import uvicorn
from user import User

app = FastAPI()
db_entity = User()  # No need to pass MySQL credentials, uses SQLite by default

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
            email=user_request['email'],  # Fixed field name
            password=user_request['password']
        )
        if user:
            return {"status": "success", "user_id": user}
        else:
            raise HTTPException(status_code=400, detail="Username or email already exists.")
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
            print("User data from DB:", user)  # Debugging
            user_id = user[0]  # Only extract the user ID
            return {"status": "success", "user_id": user_id}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
