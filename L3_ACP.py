# Parent Class
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity


# Child Class
class Bus(Vehicle):

    def fare(self):
        # Assume fare for each passenger is 100
        total_fare = self.capacity * 100

        # Add 10% maintenance charge
        total_fare += total_fare * 0.10

        return total_fare


# Create Bus Object
school_bus = Bus(50)

print("Total Bus Fare:", school_bus.fare())