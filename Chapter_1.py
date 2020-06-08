# ----------------------------------------------------------------------------------------------
# Implement a Car class that has the following attributes:
# pax_count -- number of passengers riding in the car (including the driver),
# car_mass -- mass of the empty car (in kg),
# gear_count -- number of gears.
# and method:
# total_mass - estimate mass of a car instance, assuming that an average person weight is 70 kg:
# ----------------------------------------------------------------------------------------------

class Car:

    def __init__(self, pax_count, car_mass, gear_count):

        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

    # rebuild to hold specific exceptions
    def __setattr__(self, key, value):

        if key == 'pax_count' and (value < 1 or value > 5):
            raise Exception("Number of passengers must be between 1 and 5 !")

        elif key == 'car_mass' and value > 2000:
            raise Exception("The weight of the car can't exceed 2000 kg !")

        else:
            self.__dict__[key] = value


    def total_mass(self):

        return self.car_mass + self.pax_count*70


if __name__ == '__main__':

    # test class exceptions with correct values
    test_car = Car(1, 2000, 5)
    print(test_car.total_mass())

    # test class exceptions with incorrect values
    test_car.pax_count = 2
    test_car.car_mass = 2100
    test_car.gear_count = 6








