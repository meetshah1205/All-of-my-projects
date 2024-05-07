print("*********************************")
print("You find yourself in a corridor ")
print("Where will you go? Right or Left?")
print("*********************************")

while True:
    direction = input("Right or left? ").lower()

    if direction == "right":
        print("You chose to go right.")
        print("You encounter a locked door. You need a key to proceed.")
        break

    elif direction == "left":
        print("You chose to go left.")
        print("You find a dead end. Turn back or choose another direction.")
        # The loop continues for the user to input a direction again.
    
    else:
        print("Invalid input. Please choose 'Right' or 'Left'.")
