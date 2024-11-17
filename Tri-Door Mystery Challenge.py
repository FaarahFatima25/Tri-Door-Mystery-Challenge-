import random

def play_game():
    swap_wins = 0
    swap_losses = 0
    stay_wins = 0
    stay_losses = 0

    print("Welcome to the Tri-Door Mystery Challenge!")
    while True:
        print("\nPick one of three doors. One has a car, the others have goats:\n")
        print("""
        +------+ +------+ +------+ 
        |      | |      | |      | 
        |      | |      | |      | 
        |  1   | |  2   | |  3   | 
        |      | |      | |      | 
        |      | |      | |      | 
        +------+ +------+ +------+ 
        """)

        # Randomly assign car and goat doors
        car_door = random.randint(1, 3)
        player_choice = input("Pick a door (1, 2, 3 or 'quit'): ").strip().lower()
        
        if player_choice == 'quit':
            break

        if not player_choice.isdigit() or int(player_choice) not in [1, 2, 3]:
            print("Invalid input. Please select 1, 2, 3, or type 'quit' to exit.")
            continue

        player_choice = int(player_choice)

        # Reveal a goat door
        goat_door = next(door for door in [1, 2, 3] if door != car_door and door != player_choice)
        print(f"\n+------+ +------+ +------+\nDoor {goat_door} contains a goat!")
        swap = input("Do you want to swap doors? (Y/N): ").strip().lower()

        if swap == 'y':
            # Player swaps their choice
            player_choice = next(door for door in [1, 2, 3] if door != player_choice and door != goat_door)

        # Check if the player won
        if player_choice == car_door:
            print("\nYou won!")
            if swap == 'y':
                swap_wins += 1
            else:
                stay_wins += 1
        else:
            print("\nSorry, you lost.")
            if swap == 'y':
                swap_losses += 1
            else:
                stay_losses += 1

        # Display results
        print(f"""
        Swapping: {swap_wins} wins, {swap_losses} losses, success rate {swap_wins / max(1, swap_wins + swap_losses) * 100:.1f}%
        Not swapping: {stay_wins} wins, {stay_losses} losses, success rate {stay_wins / max(1, stay_wins + stay_losses) * 100:.1f}%
        """)
        input("Press Enter to play again...")

if __name__ == "__main__":
    play_game()
