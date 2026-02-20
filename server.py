from fastapi import FastAPI

from generator import passgen

app = FastAPI()

@app.get("/json")
def passgen_json():
    password = passgen()
    return {"message": password}


