# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
_author_ = '谭华锦'


class Car():
    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.modle
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        '''通过方法改变默认值'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cat't roll back an odometer")


my_new_car = Car('china', 'a4', 2024)
# my_new_car.odometer_reading = 10
my_new_car.update_odometer(5)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = Exception('tan', 'a4', 2025)
print(my_tesla.get_descriptive_name())
