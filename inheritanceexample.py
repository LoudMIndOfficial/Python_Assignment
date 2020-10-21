class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class electricCar(Car):
    def __init__(self,make,model,year):
        #initialize attributes of the parent class
        super().__init__(make,model,year)

my_hummer = electricCar('GMC','Hummer',2022)
print(my_hummer.get_description_name())

