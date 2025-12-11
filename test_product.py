from data import product_details

def test_employee_details():
    expected_output = (
        "product Name:kitkat\n"
        "product ID:pro_1001\n"
        "Quantity:IT\n"
        "price:55000"
    )
    assert employee_details("Alice", "E1001", "IT", 55000) == expected_output
