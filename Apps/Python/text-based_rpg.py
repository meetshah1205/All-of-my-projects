print("*********************************")
print("You find yourself in a corridor ")
print("Where will you go? Right or Left?")
print("*********************************")

direction = input("Right or left? ")

if direction.lower() == "right":
    print("You chose to go right.")
    # Add the scenario for the right path here
    print("You encounter a locked door. You need a key to proceed.")
    # Your story continues...

elif direction.lower() == "left":
    print("You chose to go left.")
    # Add the scenario for the left path here
    print("You walk down the hallway and find a chest.")
    decision = input("Do you want to open the chest? (Yes/No) ")

    if decision.lower() == "yes":
        print("You found a key inside the chest!")
        # Your story continues...

    elif decision.lower() == "no":
        print("You decide to leave the chest alone and continue exploring.")
        # Your story continues...

else:
    print("Invalid input. Please choose 'Right' or 'Left'.")
