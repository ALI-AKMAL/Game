import random

choices = {"s": "Snake", "w": "Water", "g": "Gun"}

beats = {"s": "w", "w": "g", "g": "s"}

TOTAL_ROUNDS = 5
player_score = 0
computer_score = 0

print("=== SNAKE, WATER, GUN ===")
print("Snake beats Water | Water beats Gun | Gun beats Snake")
print(f"Best of {TOTAL_ROUNDS} rounds. Enter s = Snake, w = Water, g = Gun\n")

for round_no in range(1, TOTAL_ROUNDS + 1):
    print(f"--- Round {round_no} ---")

    while True:
        player = input("Your choice (s/w/g): ").strip().lower()
        if player in choices:
            break
        print("Invalid choice. Please type s, w, or g.")

    computer = random.choice(list(choices))
    print(f"You chose {choices[player]}, computer chose {choices[computer]}")

    if player == computer:
        print("It's a draw!")
    elif beats[player] == computer:
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

print("=== FINAL RESULT ===")
if player_score > computer_score:
    print("Congratulations, you won the game!")
elif computer_score > player_score:
    print("Computer won the game. Better luck next time!")
else:
    print("The game is a tie!")