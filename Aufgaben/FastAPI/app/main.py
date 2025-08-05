# main.py
from fastapi import FastAPI

app = FastAPI(title="Product API")


@app.get("/")
async def root():
    return {"message": "Product Transformation API"}
