import random
import sys

ALL_CLOSED = """
+------+ +------+ +------+ 
|      | |      | |      | 
|      | |      | |      | 
|  1   | |  2   | |  3   | 
|      | |      | |      | 
|      | |      | |      | 
+------+ +------+ +------+ """

FIRST_GOAT = """
+------+  +------+ +------+ 
|  ((  | |      | |      | 
|  00  | |      | |      | 
| /_/|_| |  2   | |  3   | 
|    | | |      | |      | 
|GOAT||| |      | |      | 
+------+  +------+ +------+ """

SECOND_GOAT = """
+------+ +------+ +------+ 
|      | |  ((  | |      | 
|      | |  00  | |      | 
|  1   | | /_/|_| |  3   | 
|      | |    | | |      | 
|      | |GOAT||| |      | 
+------+ +------+ +------+ """

THIRD_GOAT = """
+------+ +------+ +------+ 
|      | |      | |  ((  | 
|      | |      | |  00  | 
|  1   | |   2  | | /_/|_| 
|      | |      | |    | | 
|      | |      | |GOAT||| 
+------+ +------+ +------+ """

FIRST_CAR = """
+------+ +------+ +------+ 
| CAR! | |  ((  | |  ((  | 
|    __| |  00  | |  00  | 
|  _/  | | /_/|_| | /_/|_| 
| /____| |    | | |    | | 
|  O   | |GOAT||| |GOAT||| 
+------+ +------+ +------+ """

SECOND_CAR = """
+------+ +------+ +------+ 
| ((   || CAR! | |  ((  | 
|  00  ||    __| |  00  | 
| /_/|_||  _/  | | /_/|_| 
|    | || /____| |    | | 
|    ||||  O   | |GOAT||| 
+------+ +------+ +------+ """

THIRD_CAR = """
+------+ +------+ +------+ 
| ((   | | ((   | | CAR! | 
|  00  | |  00  | |    __| 
| /_/|_| | /_/|_| |  _/  | 
|    | | |    | | | /____| 
|GOAT||| |GOAT||| |  O   | 
+------+ +------+ +------+ """

print("Welcome to the Tri-Door Mystery Challenge!")
print(f"Pick one of three doors. One has a car, the others have goats:\n{ALL_CLOSED}")

swapWins = swapLosses = stayWins = stayLosses = 0

while True:
    carDoor = random.randint(1, 3)  # Assign the car to a random door
    print(ALL_CLOSED)

    # Player picks a door
    while True:
        response = input("Pick a door (1, 2, 3 or 'quit'): ").strip().lower()
        if response == 'quit':
            print("Thanks for playing!")
            sys.exit()
        if response in ['1', '2', '3']:
            chosenDoor = int(response)
            break

    # Reveal a goat door
    while True:
        goatDoor = random.randint(1, 3)
        if goatDoor != chosenDoor and goatDoor != carDoor:
            break

    # Show the goat
    if goatDoor == 1:
        print(FIRST_GOAT)
    elif goatDoor == 2:
        print(SECOND_GOAT)
    elif goatDoor == 3:
        print(THIRD_GOAT)

    print(f"Door {goatDoor} contains a goat!")

    # Ask the player if they want to swap
    while True:
        swap = input("Do you want to swap doors? (Y/N): ").strip().upper()
        if swap in ['Y', 'N']:
            break

    # Handle swapping logic
    if swap == 'Y':
        chosenDoor = 6 - chosenDoor - goatDoor  # Compute the remaining unopened door

    # Reveal where the car was
    if carDoor == 1:
        print(FIRST_CAR)
    elif carDoor == 2:
        print(SECOND_CAR)
    elif carDoor == 3:
        print(THIRD_CAR)

    print(f"The car was behind Door {carDoor}!")

    # Determine the outcome
    if chosenDoor == carDoor:
        print("You won!")
        if swap == 'Y':
            swapWins += 1
        else:
            stayWins += 1
    else:
        print("Sorry, you lost.")
        if swap == 'Y':
            swapLosses += 1
        else:
            stayLosses += 1

    # Show statistics
    totalSwaps = swapWins + swapLosses
    swapSuccess = round(swapWins / totalSwaps * 100, 1) if totalSwaps > 0 else 0.0
    totalStays = stayWins + stayLosses
    staySuccess = round(stayWins / totalStays * 100, 1) if totalStays > 0 else 0.0

    print(f"\nSwapping: {swapWins} wins, {swapLosses} losses, success rate {swapSuccess}%")
    print(f"Not swapping: {stayWins} wins, {stayLosses} losses, success rate {staySuccess}%\n")

    # Prompt to play again
    input("Press Enter to play again...")
