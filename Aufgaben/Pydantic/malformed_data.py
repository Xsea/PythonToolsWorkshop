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
