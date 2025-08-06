from datetime import datetime

from pydantic import BaseModel


class InternalProduct(BaseModel):
    product_id: int
    name: str
    current_price: float
    acquisition_timestamp: datetime
    status: str
