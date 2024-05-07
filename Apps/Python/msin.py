import random

player_health = 100
enemy_health = 100

while player_health > 0 and enemy_health > 0:
    print("Your health:", player_health)
    print("Enemy's health:", enemy_health)
    print("1. Shoot")
    print("2. Dodge")
    
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        damage = random.randint(10, 25)
        enemy_health -= damage
        print("You dealt", damage, "damage to the enemy!")
    elif choice == "2":
        dodge_chance = random.random()
        if dodge_chance < 0.5:
            print("You successfully dodged the enemy's attack!")
        else:
            damage = random.randint(10, 20)
            player_health -= damage
            print("You failed to dodge and took", damage, "damage from the enemy!")
    else:
        print("Invalid choice. Please enter 1 or 2.")

    if player_health <= 0:
        print("You are defeated. Game over!")
    elif enemy_health <= 0:
        print("You defeated the enemy! You win!")
