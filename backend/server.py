from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from generator import passgen

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/json")
def passgen_json():
    password = passgen()
    return {"message": password}


