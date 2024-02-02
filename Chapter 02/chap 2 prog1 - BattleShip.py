import random

battle_pattern = []

for i in range(5):
    battle_pattern.append(['O '] * 5)

def display(pattern):
    for p in pattern:
        print(" ".join(p))

print("Battleship Challenge - GAME ON!")
display(battle_pattern)

def get_random_row(pattern):
    return random.randint(0, len(pattern) - 1)

def get_random_col(pattern):
    return random.randint(0, len(pattern[0]) - 1)

ship_row = get_random_row(battle_pattern)
ship_col = get_random_col(battle_pattern)
print(f"hint: row={ship_row}, col={ship_col}")

for option in range(4):
    input_row = int(input("Enter Guess Row (Starts with 0):"))
    input_col = int(input("Enter Guess Col (Starts with 0):"))

    if input_row == ship_row and input_col == ship_col:
        print("You Win! You sunk my battleship!")
        break
    else:
        if option == 3:
            battle_pattern[input_row][input_col] = "X "
            display(battle_pattern)
            print("Sorry Player... Game Over!")
            print("\nShip is here: [" + str(ship_row) + "]["+ str(ship_col) + "]")
        else:
            if (input_row < 0 or input_row > 4) or (input_col <0 or input_col > 4):
                print("Where did you fire ? Over the ocean.")
            elif (battle_pattern[input_row][input_col] == "X"):
                print("You have already got that wrong.")
            else:
                print("You totally missed my battleship!")
                battle_pattern[input_row][input_col] = "X "
            print("Attempt : ",option + 1)
            display(battle_pattern)

