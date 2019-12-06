# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is Main Class
class Vehicle():
    def __init__(self):
        pass

# GroundVehicle(Vehicle)
class GroundVehicle(Vehicle):
    def __init__(self):
        # Inside parathensis below would be attributes from parent class
        super().__init__()
        pass

# Car(GroundVehicle) nested from Vehicle
class Car(GroundVehicle):
    def __init__(self):
        # Inside parathensis below would be attributes from parent class
        super().__init__()
        pass

# Motorcycle(GroundVehicle) nested from Vehicle
class Motorcycle(GroundVehicle):
    def __init__(self):
        # Inside parathensis below would be attributes from parent class
        super().__init__()
        pass

# Flight Vehicle(Vehicle)
class FlightVehicle(Vehicle):
    def __init__(self):
        # Inside parathensis below would be attributes from parent class
        super().__init__()
        pass

# Airplane(FlightVehicle) nested from Vehicle
class Airplane(FlightVehicle):
    def __init__(self):
         # Inside parathensis below would be attributes from parent class
        super().__init__()
        pass

# Starship(FlightVehicle) nested from Vehicle
class Starship(FlightVehicle):
    def __init__(self):
         # Inside parathensis below would be attributes from parent class
        super().__init__()
        pass
