# OOPs Concepts
""" OOPS Principles: 1. Classes
                     2. Objects
                     3. Inheritance
                     4. Encapsulation
                     5. Polymorphism
                     6. Abstraction"""

""" OOPs is a way of organizing code that uses objects and classes to represent real-world entiies """

# 1. CLASSES
""" Class is collection of objects... they are blueprints for creating objects, It defines a set of attributes and methods that created objects can have.
1. Classes are created by keywords
2. Attributes are variables that belong to a class
3. Attributes are always public and can be accessed using a dot(.) operator
Aviationclass.Aviationattribute"""
class Aircraft:
    # Class attribute
    category = "Aviation"

    def __init__(self, model, capacity, manufacturer):
        # Instance attributes
        self.model = model
        self.capacity = capacity
        self.manufacturer = manufacturer

#OBJECTS --- These are instances of the class
""" Object consists of:
1. State: Rep. by attributes and reflects the properties of an object
2. behaviour: Rep. by methods of an object and reflects response of object to other objects
3. Identity: Gives unique name to an object and enables one object to interact with other objects."""
# Create instances of the Aircraft class
aircraft1 = Aircraft("Boeing 737", 160, "Boeing")
aircraft2 = Aircraft("Airbus A320", 180, "Airbus")
aircraft3 = Aircraft("Cessna 172", 4, "Cessna")
# Accessing class and instance attributes
print(f"{aircraft1.model} is a {Aircraft.category} vehicle with a capacity of {aircraft1.capacity} passengers, manufactured by {aircraft1.manufacturer}.")
print(f"{aircraft2.model} is a {Aircraft.category} vehicle with a capacity of {aircraft2.capacity} passengers, manufactured by {aircraft2.manufacturer}.")
print(f"{aircraft3.model} is a {Aircraft.category} vehicle with a capacity of {aircraft3.capacity} passengers, manufactured by {aircraft3.manufacturer}.")
""" O/P: 
Boeing 737 is a Aviation vehicle with a capacity of 160 passengers, manufactured by Boeing.
Airbus A320 is a Aviation vehicle with a capacity of 180 passengers, manufactured by Airbus.
Cessna 172 is a Aviation vehicle with a capacity of 4 passengers, manufactured by Cessna."""

#SELF PARAMETER --- Ref. to the current instance of the class, it allows to access the attributes and methods of the object.
# __init__ method --- is constructor in python, automatically called when a new object is created, it initializes the attributes of the class.
class Aircraft:
    # Class attribute
    category = "Aviation"
    def __init__(self, model, capacity, manufacturer): 
        # Using `self` to assign values to instance attributes
        self.model = model
        self.capacity = capacity
        self.manufacturer = manufacturer
    # Instance method using `self`
    def display_details(self):
        print(f"Model: {self.model}")
        print(f"Capacity: {self.capacity}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Category: {self.category}\n")  # Accessing the class attribute using self
    # Another instance method using `self`
    def is_large_aircraft(self):
        if self.capacity > 150:
            return f"{self.model} is a large aircraft."
        else:
            return f"{self.model} is a small aircraft."
# Create instances of Aircraft
aircraft1 = Aircraft("Boeing 737", 160, "Boeing")
aircraft2 = Aircraft("Cessna 172", 4, "Cessna")
aircraft3 = Aircraft("Airbus A380", 853, "Airbus")
# Call instance methods that use `self`
aircraft1.display_details()
aircraft2.display_details()
aircraft3.display_details()
print(aircraft1.is_large_aircraft())
print(aircraft2.is_large_aircraft())
print(aircraft3.is_large_aircraft())
""" o/p: 
Model: Boeing 737
Capacity: 160
Manufacturer: Boeing
Category: Aviation

Model: Cessna 172
Capacity: 4
Manufacturer: Cessna
Category: Aviation

Model: Airbus A380
Capacity: 853
Manufacturer: Airbus
Category: Aviation

Boeing 737 is a large aircraft.
Cessna 172 is a small aircraft.
Airbus A380 is a large aircraft."""

# CLASS & INSTANCE VARIABLES
""" Variables defined in a class can be either class variables or instance variables
1. CLASS VARIABLES : Variables that are shared across all instances of a class, defined outside any methods. Unless overidden by a object they all share the same value for a class variable...

2. INSTANCE VARIABLE: Variables that are unique to each instance(object) of a class. These are defined within __init__ method or other instance methods."""
class Aircraft:
    # Class variable (shared across all instances)
    category = "Aviation"
    def __init__(self, model, capacity, manufacturer):
        # Instance variables (specific to each instance)
        self.model = model
        self.capacity = capacity
        self.manufacturer = manufacturer
    # Method to display details
    def display_details(self):
        print(f"Model: {self.model}")
        print(f"Capacity: {self.capacity}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Category: {Aircraft.category}\n")  # Accessing class variable directly
    # Method to demonstrate modifying instance variables
    def update_capacity(self, new_capacity):
        self.capacity = new_capacity  # Modifies the instance variable
        print(f"Updated capacity of {self.model}: {self.capacity}")
    # Method to demonstrate modifying class variables
    @classmethod
    def update_category(cls, new_category):
        cls.category = new_category  # Modifies the class variable
        print(f"Updated category for all aircraft: {cls.category}")
# Create instances of Aircraft
aircraft1 = Aircraft("Boeing 737", 160, "Boeing")
aircraft2 = Aircraft("Cessna 172", 4, "Cessna")
# Access class and instance variables
print("Before updates:")
aircraft1.display_details()
aircraft2.display_details()
# Update instance variable for aircraft1
aircraft1.update_capacity(180)
# Update class variable (affects all instances)
Aircraft.update_category("Commercial Aviation")
print("\nAfter updates:")
aircraft1.display_details()
aircraft2.display_details()
""" O/P: Before updates:
Model: Boeing 737
Capacity: 160
Manufacturer: Boeing
Category: Aviation

Model: Cessna 172
Capacity: 4
Manufacturer: Cessna
Category: Aviation

Updated capacity of Boeing 737: 180
Updated category for all aircraft: Commercial Aviation

After updates:
Model: Boeing 737
Capacity: 180
Manufacturer: Boeing
Category: Commercial Aviation

Model: Cessna 172
Capacity: 4
Manufacturer: Cessna
Category: Commercial Aviation """

# INHERITANCE --- allows a class to acquire properties and methods of another class. 
""" Types of inheritance: 
1. Single Inheritance: a child inherites from single parent class
2. Mulitple Inheritance: a child class inherits from more than one parent class
3. Multilevel Inheritance: a child class inherts from parent class, which in turn inherits from another class. 
4. Hierarchical Inheritance: multiple child classes inherit from a single parent class
5. Hybrid Inheritance: a combination of two or more types of inheritance. """
# Single Inheritance
class Aircraft:
    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer
    def aircraft_info(self):
        return f"Aircraft Model: {self.model}, Manufacturer: {self.manufacturer}"
class CommercialAircraft(Aircraft):  # Single inheritance
    def __init__(self, model, manufacturer, capacity):
        super().__init__(model, manufacturer)
        self.capacity = capacity
    def commercial_info(self):
        return f"Capacity: {self.capacity} passengers"
# Multiple Inheritance
class MaintenanceSchedule:
    def __init__(self, maintenance_date):
        self.maintenance_date = maintenance_date
    def maintenance_info(self):
        return f"Next Maintenance Date: {self.maintenance_date}"
class CargoAircraft(Aircraft, MaintenanceSchedule):  # Multiple inheritance
    def __init__(self, model, manufacturer, cargo_capacity, maintenance_date):
        Aircraft.__init__(self, model, manufacturer)
        MaintenanceSchedule.__init__(self, maintenance_date)
        self.cargo_capacity = cargo_capacity
    def cargo_info(self):
        return f"Cargo Capacity: {self.cargo_capacity} tons"
# Multilevel Inheritance
class FighterAircraft(Aircraft):
    def __init__(self, model, manufacturer, max_speed):
        super().__init__(model, manufacturer)
        self.max_speed = max_speed
    def fighter_info(self):
        return f"Max Speed: {self.max_speed} km/h"
class StealthFighter(FighterAircraft):  # Multilevel inheritance
    def __init__(self, model, manufacturer, max_speed, radar_visibility):
        super().__init__(model, manufacturer, max_speed)
        self.radar_visibility = radar_visibility
    def stealth_info(self):
        return f"Radar Visibility: {self.radar_visibility}"
# Hierarchical Inheritance
class PrivateJet(Aircraft):  # Hierarchical inheritance
    def __init__(self, model, manufacturer, owner):
        super().__init__(model, manufacturer)
        self.owner = owner
    def private_jet_info(self):
        return f"Owner: {self.owner}"
# Hybrid Inheritance
class HybridAircraft(CargoAircraft, StealthFighter):  # Hybrid inheritance
    def __init__(self, model, manufacturer, cargo_capacity, maintenance_date, max_speed, radar_visibility):
        CargoAircraft.__init__(self, model, manufacturer, cargo_capacity, maintenance_date)
        StealthFighter.__init__(self, model, manufacturer, max_speed, radar_visibility)
    def hybrid_info(self):
        return "Hybrid Aircraft: Combines cargo and stealth capabilities"
# Testing the examples
# Single Inheritance
commercial = CommercialAircraft("Boeing 737", "Boeing", 180)
print(commercial.aircraft_info())
print(commercial.commercial_info())
# Multiple Inheritance
cargo = CargoAircraft("C-130 Hercules", "Lockheed Martin", 20, "2025-01-15")
print(cargo.aircraft_info())
print(cargo.maintenance_info())
print(cargo.cargo_info())
# Multilevel Inheritance
stealth = StealthFighter("F-35 Lightning II", "Lockheed Martin", 1930, "Low")
print(stealth.aircraft_info())
print(stealth.fighter_info())
print(stealth.stealth_info())
# Hierarchical Inheritance
private = PrivateJet("Gulfstream G650", "Gulfstream Aerospace", "Elon Musk")
print(private.aircraft_info())
print(private.private_jet_info())
# Hybrid Inheritance
hybrid = HybridAircraft("HybridJet X", "AviationTech", 25, "2025-02-01", 1500, "Very Low")
print(hybrid.aircraft_info())
print(hybrid.maintenance_info())
print(hybrid.cargo_info())
print(hybrid.stealth_info())
print(hybrid.hybrid_info())
""" O/P:
Aircraft Model: Boeing 737, Manufacturer: Boeing
Capacity: 180 passengers

Aircraft Model: C-130 Hercules, Manufacturer: Lockheed Martin
Next Maintenance Date: 2025-01-15
Cargo Capacity: 20 tons

Aircraft Model: F-35 Lightning II, Manufacturer: Lockheed Martin
Max Speed: 1930 km/h
Radar Visibility: Low

Aircraft Model: Gulfstream G650, Manufacturer: Gulfstream Aerospace
Owner: Elon Musk

Aircraft Model: HybridJet X, Manufacturer: AviationTech
Next Maintenance Date: 2025-02-01
Cargo Capacity: 25 tons
Radar Visibility: Very Low
Hybrid Aircraft: Combines cargo and stealth capabilities """

# POLYMORPHISM -- Allows methods to have same name but behave differently based on object's contex, Can be achieved through method overridding or overloading..
""" TYPES OF POLYMORPHISM:
1. Compile-Time Polymorphism(method overloading): determined during runtime of the program, It allows methods or operators with the same name to behave differently based on their input parameters or usage. It is commonly referred to as method or operator overloading.
2. Run-Time Polymorphism (method overriding) :determined during the execution of the program. It occurs when a subclass provides a specific implementation for a method already defined in its parent class, commonly known as method overriding."""

# Compile-Time Polymorphism (Method Overloading)
class Aircraft:
    def fly(self, speed=None, altitude=None):
        if speed is not None and altitude is not None:
            return f"Flying at {speed} km/h at an altitude of {altitude} feet."
        elif speed is not None:
            return f"Flying at {speed} km/h."
        else:
            return "Flying at standard speed."
# Run-Time Polymorphism (Method Overriding)
class PassengerAircraft(Aircraft):
    def fly(self, speed=None, altitude=None):
        return "Passenger aircraft is flying with a focus on comfort."
class FighterAircraft(Aircraft):
    def fly(self, speed=None, altitude=None):
        return "Fighter aircraft is flying with maximum agility and speed."
# Testing Compile-Time Polymorphism
print("=== Compile-Time Polymorphism ===")
plane = Aircraft()
print(plane.fly())  # Default method
print(plane.fly(500))  # Overloaded with speed
print(plane.fly(700, 30000))  # Overloaded with speed and altitude
# Testing Run-Time Polymorphism
print("\n=== Run-Time Polymorphism ===")
passenger_plane = PassengerAircraft()
fighter_plane = FighterAircraft()
print(passenger_plane.fly())  # Overridden method in PassengerAircraft
print(fighter_plane.fly())  # Overridden method in FighterAircraft
"""O/P:
=== Compile-Time Polymorphism ===
Flying at standard speed.
Flying at 500 km/h.
Flying at 700 km/h at an altitude of 30000 feet.

=== Run-Time Polymorphism ===
Passenger aircraft is flying with a focus on comfort.
Fighter aircraft is flying with maximum agility and speed."""

# ENCAPSULATION: building of data(attributes and methods (functions) within a class
""" TYPES OF ENCAPSULATION:
1. Public Members: accessible from anywhere
2. Protected Mmebers: accessible within class and its subclass
3. Private Mmebers: accessible only within the class.."""
class Aircraft:
    def __init__(self, name, capacity, secret_code):
        self.name = name  # Public member
        self._capacity = capacity  # Protected member
        self.__secret_code = secret_code  # Private member
    def display_public(self):
        return f"Aircraft Name: {self.name}"  # Public method
    def _display_protected(self):
        return f"Capacity: {self._capacity} passengers"  # Protected method
    def __display_private(self):
        return f"Secret Code: {self.__secret_code}"  # Private method
    def access_private(self):
        return self.__display_private()  # Accessing private method within the class
# Subclass demonstrating protected access
class CargoAircraft(Aircraft):
    def display_protected(self):
        return f"Cargo Aircraft Capacity: {self._capacity} tons"  # Accessing protected member
# Creating an object of the Aircraft class
plane = Aircraft("Boeing 747", 400, "XYZ123")
# Public member access
print("=== Public Members ===")
print(plane.name)  # Accessing public member
print(plane.display_public())  # Accessing public method
# Protected member access
print("\n=== Protected Members ===")
# Accessible directly, though not recommended
print(plane._capacity)  # Accessing protected member directly
# Accessible through a method in subclass
cargo_plane = CargoAircraft("C-130 Hercules", 20, "ABC987")
print(cargo_plane.display_protected())
# Private member access
print("\n=== Private Members ===")
# Cannot access directly
# print(plane.__secret_code)  # Uncommenting this will raise an AttributeError
# print(plane.__display_private())  # Uncommenting this will raise an AttributeError
# Access through a public method within the class
print(plane.access_private())
""" O/P: 
Passenger aircraft is flying with a focus on comfort.
Fighter aircraft is flying with maximum agility and speed.
=== Public Members ===
Boeing 747
Aircraft Name: Boeing 747

=== Protected Members ===
400
Cargo Aircraft Capacity: 20 tons

=== Private Members ===
Secret Code: XYZ123"""

# DATA ABSTRACTION --- Hides internal imlementation details while exposing only necessary functionality. Helps focus on "what to do" rather than "how to do"
""" TYPES OF ABSTRACTION
1. Partial Abstraction: Abstraction class contains both abstarct and concrete methods
2. Full Abstraction: Abstract class contains only abstract methods (like interfaces)."""
from abc import ABC, abstractmethod
# Partial Abstraction: Abstract class with both abstract and concrete methods
class Aircraft(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def fly(self):  # Abstract method (must be implemented by subclasses)
        pass
    def info(self):  # Concrete method (already implemented)
        return f"This is the aircraft: {self.name}"
class PassengerAircraft(Aircraft):
    def fly(self):
        return f"{self.name} is flying passengers at cruising altitude."
class CargoAircraft(Aircraft):
    def fly(self):
        return f"{self.name} is transporting cargo to its destination."
# Full Abstraction: Abstract class with only abstract methods (like an interface)
class AirportServices(ABC):
    @abstractmethod
    def provide_fuel(self):
        pass
    @abstractmethod
    def handle_baggage(self):
        pass
class LargeAirport(AirportServices):
    def provide_fuel(self):
        return "Fuel provided to all large aircraft."
    def handle_baggage(self):
        return "Baggage handled efficiently for all flights."
class SmallAirport(AirportServices):
    def provide_fuel(self):
        return "Limited fuel provided for small aircraft only."
    def handle_baggage(self):
        return "Minimal baggage handling service available."
# Testing Partial Abstraction
print("=== Partial Abstraction ===")
passenger_plane = PassengerAircraft("Boeing 737")
cargo_plane = CargoAircraft("C-130 Hercules")
print(passenger_plane.fly())
print(passenger_plane.info())
print(cargo_plane.fly())
print(cargo_plane.info())
# Testing Full Abstraction
print("\n=== Full Abstraction ===")
large_airport = LargeAirport()
small_airport = SmallAirport()
print(large_airport.provide_fuel())
print(large_airport.handle_baggage())
print(small_airport.provide_fuel())
print(small_airport.handle_baggage())
"""O/P: 
=== Partial Abstraction ===
Boeing 737 is flying passengers at cruising altitude.
This is the aircraft: Boeing 737
C-130 Hercules is transporting cargo to its destination.
This is the aircraft: C-130 Hercules

=== Full Abstraction ===
Fuel provided to all large aircraft.
Baggage handled efficiently for all flights.
Limited fuel provided for small aircraft only.
Minimal baggage handling service available."""


