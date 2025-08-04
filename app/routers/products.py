# routers/products.py
import asyncio
from typing import Dict, List

from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.models.external_product import ExternalProduct
from app.models.internal_product import InternalProduct

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Product not found"}},
)

# In-memory database to store products
product_db: Dict[int, InternalProduct] = {}


async def process_product(external_product: ExternalProduct):
    # Transform the product
    internal_product = InternalProduct.from_external(external_product)

    # Simulate some processing time
    await asyncio.sleep(15)

    # Store the transformed product in our in-memory database
    product_db[internal_product.product_id] = internal_product

    print(
        f"Product {internal_product.name} (ID: {internal_product.product_id}) processed and stored in database"
    )


@router.post("/transform")
async def transform_product(
    external_product: ExternalProduct, background_tasks: BackgroundTasks
):
    # Add the product processing task to run in the background
    background_tasks.add_task(process_product, external_product)

    # Return an immediate success response
    return {
        "message": f"Product transformation request received for {external_product.product_name}",
    }


@router.get("/", response_model=List[InternalProduct])
async def get_all_products():
    return list(product_db.values())


@router.get("/{product_id}", response_model=InternalProduct)
async def get_product(product_id: int):
    if product_id not in product_db:
        raise HTTPException(
            status_code=404, detail=f"Product with ID {product_id} not found"
        )

    return product_db[product_id]
