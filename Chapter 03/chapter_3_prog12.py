class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def calculate_total_cost(self):
        # calculate total cost here
        return 100

#calling
my_car = Vehicle("Honda", "Civic")
total_cost = my_car.calculate_total_cost()
print("Total cost: ",total_cost)

