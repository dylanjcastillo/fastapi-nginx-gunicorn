# Create hello world FastAPI app
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"app_status": "It's working!"}
