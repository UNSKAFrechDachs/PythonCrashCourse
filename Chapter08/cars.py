def make_car(manufacturer, model, **car_information):
    car_information['manufacturer'] = manufacturer
    car_information['model'] = model
    return car_information

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)