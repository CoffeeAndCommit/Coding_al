# Assignment: Dog Breed
# Create a Dog class with one class variable and two instance variables,
# and display the details of dogs of two different breeds.

class Dog:
    # Class variable (shared by all instances)
    species = "Canis lupus familiaris"

    # Constructor with two instance variables
    def __init__(self, breed, name):
        self.breed = breed  # Instance variable 1
        self.name = name    # Instance variable 2

    # Method to display dog details
    def display_details(self):
        print(f"Name   : {self.name}")
        print(f"Breed  : {self.breed}")
        print(f"Species: {self.species}")


# Creating two Dog objects of different breeds
dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("German Shepherd", "Rocky")

# Displaying details
print("--- Dog 1 Details ---")
dog1.display_details()

print()

print("--- Dog 2 Details ---")
dog2.display_details()
