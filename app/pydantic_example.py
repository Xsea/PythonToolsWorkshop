import datetime

from app.models.external_product import ExternalProduct
from app.models.internal_product import InternalProduct

valid_data = {
    "item_id": 101,
    "productName": "Laptop",
    "initial_price": "1200.50",
    "received_date": "25.10.1991",
}

product = ExternalProduct(**valid_data)
print(f"Valid product created: {product}")
print(f"Item ID: {product.item_id}")
print(f"Product Name: {product.product_name}")
print(f"Initial Price: {product.initial_price}")
print(f"Received Date: {product.received_date}")
print(product.model_dump())

try:
    invalid_data1 = {
        "item_id": "abc",  # Should be an integer
        "productName": "Laptop",
        "initial_price": "1200.50",
        "received_date": "2024-01-15T10:30:00",
    }
    product = ExternalProduct(**invalid_data1)
except Exception as e:
    print(f"Validation Error for invalid item_id:\n{e}")

try:
    invalid_data2 = {
        "item_id": 101,
        "productName": "Laptop",
        # Missing initial_price
        "received_date": "2024-01-15T10:30:00",
    }
    product = ExternalProduct(**invalid_data2)
except Exception as e:
    print(f"Validation Error for missing field:\n{e}")

try:
    invalid_data3 = {
        "item_id": 101,
        "productName": "Laptop",
        "initial_price": "1200.50",
        "received_date": "15-01-2024",  # Wrong format
    }
    product = ExternalProduct(**invalid_data3)
    print(f"Received Date: {product.received_date}")
except Exception as e:
    print(f"Validation Error for invalid date format:\n{e}")

external_product = ExternalProduct(
    item_id=1001,
    productName="Wireless Headphones",
    initial_price="129.99",  # Price as string
    received_date=datetime.datetime(2023, 5, 15, 14, 30),
)

# Transform to InternalProduct
internal_product = InternalProduct.from_external(external_product)

# Print the result using model_dump()
print(internal_product.model_dump())

# Explicitly show the type conversion
print(f"\nType of external price: {type(external_product.initial_price)}")
print(f"Type of internal price: {type(internal_product.current_price)}")
print(f"Value of internal price: {internal_product.current_price}")
print(f"Value of internal date: {internal_product.acquisition_timestamp}")

# Create sample data
sample_data = {
    "item_id": 1001,
    "productName": "Ergonomic Keyboard",
    "initial_price": "$89.99",
    "received_date": "2023-05-15T14:30:00",
    "supplier": {
        "supplier_id": 501,
        "name": "TechSupplies Inc.",
        "contactEmail": "info@techsupplies.com",
        "rating": 4.8,
    },
}


# Create and validate the model instance
product = ExternalProduct(**sample_data)
print(product.model_dump(by_alias=True))
