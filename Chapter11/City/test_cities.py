from city_functions import format_city_country


def test_city_country():
    formatted_string = format_city_country(city='santiago', country='Chile')
    assert formatted_string == "Santiago, Chile"


def test_city_country_population():
    formatted_string = format_city_country(city='santiago', country='Chile', population=5_000_000)
    assert formatted_string == "Santiago, Chile - population 5000000"
