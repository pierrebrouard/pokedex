from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "This is the Pokedex Project backend coded using FastAPI"}
