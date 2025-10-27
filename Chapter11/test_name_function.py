from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name("john", "doe")
    assert formatted_name == "Doe, John"

def test_first_last_middle_name():
    formatted_name = get_formatted_name("john", "doe", "smith")
    assert formatted_name == "Doe, John Smith"