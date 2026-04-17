from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/health")
async def health():
    return {"message": "healthy"}

@app.get("/me")
async def me():
    return {
        "name": "Shittu Ayomide Idris",  # Update this
        "email": "ayorexyshittu@gmail.com", # Update this
        "github": "https://github.com/lazyturd" # Update this
    }
