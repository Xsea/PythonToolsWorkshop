valid_data = {
    "item_id": 101,
    "product_Name": "Laptop",
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
