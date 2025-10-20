def describe_city(name, country="Germany"):
    print(f"{name.title()} is in {country.title()}.")

describe_city("Berlin")
describe_city("Cologne")
describe_city(name="albuquerque", country="USA")