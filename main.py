from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Health AI Backend Running"}
