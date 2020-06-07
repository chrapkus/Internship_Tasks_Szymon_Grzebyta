# First Task - creation of Car class

class Car:

    def __init__(self, pax_count, car_mass, gear_count):

        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count


    def __setattr__(self, key, value):

        if key == 'pax_count' and (value < 1 or value > 5):
            raise Exception("Number of passengers must be between 1 and 5 !")

        elif key == 'car_mass' and value > 2000:
            raise Exception("The weight of the car can't exceed 2000 kg !")

        else:
            self.__dict__[key] = value


    def total_mass(self):

        return self.car_mass + self.pax_count*70

t = Car(1, 2000, 5)
print(t)




