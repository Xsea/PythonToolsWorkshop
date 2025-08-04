# main.py
from fastapi import FastAPI

from app.routers import products

app = FastAPI(title="Product API")

# Include the products router
app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Product Transformation API"}
