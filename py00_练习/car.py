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