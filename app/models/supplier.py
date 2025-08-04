from pydantic import BaseModel, Field


class Supplier(BaseModel):
    supplier_id: int
    name: str
    contact_email: str = Field(alias="contactEmail")
    rating: float
