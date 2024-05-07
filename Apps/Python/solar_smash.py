import random

class CelestialBody:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        self.destroyed = False

    def impact(self, energy):
        destruction_chance = min(1.0, energy / self.mass)
        if random.random() < destruction_chance:
            self.destroyed = True

sun = CelestialBody("Sun", 1.989e30)
earth = CelestialBody("Earth", 5.972e24)

print("Welcome to Text-Based Celestial Smash!")
print("Choose a celestial body to attack: 1 - Sun, 2 - Earth")

choice = int(input("Enter your choice: "))

if choice == 1:
    target = sun
else:
    target = earth

print(f"You've selected {target.name}.")
energy = float(input("Enter the energy of impact: "))

target.impact(energy)

if target.destroyed:
    print(f"{target.name} has been destroyed!")
else:
    print(f"{target.name} survived the impact.")

print("Thanks for playing!")
