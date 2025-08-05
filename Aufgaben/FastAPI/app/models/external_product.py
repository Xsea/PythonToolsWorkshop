from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from Aufgaben.FastAPI.app.models.supplier import Supplier


class ExternalProduct(BaseModel):
    item_id: int
    product_name: str = Field(alias="productName")
    initial_price: str
    received_date: datetime
    supplier: Optional[Supplier] = None

    # Field validator to handle German date format (DD.MM.YYYY)
    @field_validator("received_date", mode="before")
    @classmethod
    def parse_german_date(cls, value):
        if isinstance(value, str) and "." in value:
            try:
                # Parse German date format (DD.MM.YYYY)
                day, month, year = map(int, value.split("."))
                return datetime(year, month, day)
            except (ValueError, TypeError):
                raise ValueError(
                    f"Invalid German date format: {value}. Expected DD.MM.YYYY"
                )
        return value  # Return as is if already datetime
