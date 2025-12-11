def product_details(name,pro_id,quantity, price):
    result = (
        f"Product Name:{name}\n"
        f"Product ID:{pro_id}\n"
        f"Quantity:{quantity}\n"
        f"Price:{price}"
    )
    return result

if __name__ == "__main__":
    name = "kitkat"
    pro_id = "p1001"
    quantity = "30g"
    salary = 20
    print(product_details(name,pro_id,quantity, price))

