# A simple Dog class example for beginners

class Dog:
    """
    This is a simple Dog class that demonstrates basic OOP concepts.
    A class is like a blueprint for creating objects (instances).
    """
    
    # Class variable - shared by all instances of the class
    species = "Canis familiaris"  # All dogs belong to this species
    
    def __init__(self, name, age, breed):
        """
        This is the constructor method (__init__).
        It runs automatically when you create a new Dog object.
        'self' refers to the specific instance being created.
        
        Parameters:
        name (str): The dog's name
        age (int): The dog's age in years  
        breed (str): The dog's breed
        """
        # Instance variables - unique to each dog object
        self.name = name      # Each dog has its own name
        self.age = age        # Each dog has its own age
        self.breed = breed    # Each dog has its own breed
        self.is_sleeping = False  # Default state - dog is awake
    
    def bark(self):
        """
        This is an instance method - a function that belongs to the class.
        It can access and modify the object's data using 'self'.
        """
        return f"{self.name} says: Woof! Woof!"
    
    def sleep(self):
        """
        Method to make the dog sleep.
        This changes the dog's state.
        """
        self.is_sleeping = True
        return f"{self.name} is now sleeping... Zzz"
    
    def wake_up(self):
        """
        Method to wake up the dog.
        """
        self.is_sleeping = False
        return f"{self.name} is now awake and ready to play!"
    
    def get_info(self):
        """
        Method that returns information about the dog.
        Shows how methods can return formatted strings with object data.
        """
        status = "sleeping" if self.is_sleeping else "awake"
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}, Status: {status}"
    
    def have_birthday(self):
        """
        Method that increases the dog's age by 1.
        Shows how methods can modify object data.
        """
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old!"


# HOW TO USE THE CLASS:

# Creating objects (instances) of the Dog class
print("=== Creating Dog Objects ===")
dog1 = Dog("Buddy", 3, "Golden Retriever")  # Create first dog
dog2 = Dog("Max", 5, "German Shepherd")     # Create second dog

# Accessing object data
print(f"Dog 1: {dog1.name} is a {dog1.age}-year-old {dog1.breed}")
print(f"Dog 2: {dog2.name} is a {dog2.age}-year-old {dog2.breed}")

# Calling methods on objects
print("\n=== Calling Methods ===")
print(dog1.bark())        # Buddy says: Woof! Woof!
print(dog2.bark())        # Max says: Woof! Woof!

# Changing object state
print("\n=== Changing States ===")
print(dog1.sleep())       # Buddy is now sleeping...
print(dog1.get_info())    # Shows Buddy is sleeping

print(dog1.wake_up())     # Buddy is now awake and ready to play!
print(dog1.get_info())    # Shows Buddy is awake

# Modifying object data
print("\n=== Having Birthdays ===")
print(dog1.have_birthday())  # Happy Birthday Buddy! You are now 4 years old!
print(dog2.have_birthday())  # Happy Birthday Max! You are now 6 years old!

# Accessing class variables
print(f"\n=== Class Variable ===")
print(f"All dogs belong to species: {Dog.species}")
print(f"Buddy's species: {dog1.species}")  # Can also access through instance
