from product import product_details

def test_product_details():                                                                                 
    expected_output = (
        "Product Name:kitkat\n"
        "Product ID:p1001\n"
        "Quantity:20g\n"
        "Price:20"
    )
    assert product_details("kitkat","p1001","20g", 20) == expected_output


