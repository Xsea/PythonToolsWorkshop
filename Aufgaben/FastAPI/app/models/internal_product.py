from datetime import datetime

from pydantic import BaseModel, Field, computed_field

from Aufgaben.FastAPI.app.models.external_product import ExternalProduct


class InternalProduct(BaseModel):
    product_id: int = Field(gt=0, description="Product ID must be greater than 0")
    name: str
    current_price: float
    acquisition_timestamp: datetime

    @computed_field
    @property
    def status(self) -> str:
        return (
            "new"
            if (datetime.now() - self.acquisition_timestamp).days <= 30
            else "regular"
        )

    @classmethod
    def from_external(cls, external: ExternalProduct) -> "InternalProduct":
        return cls(
            product_id=external.item_id,
            name=external.product_name,
            current_price=external.initial_price,  # String to float coercion happens here
            acquisition_timestamp=external.received_date,
        )
