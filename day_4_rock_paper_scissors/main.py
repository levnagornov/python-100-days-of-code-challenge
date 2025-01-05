import random


def main() -> None:
    print("""Welcome to my Rock-Paper-Scissors game!
    Make your choice:
    1 - 👊 Rock
    2 - ✋ Paper
    3 - ✌️ Scissors
    """)

    rock_option: int = 1
    paper_option: int = 2
    scissors_option: int = 3
    valid_options: list[int] = [rock_option, paper_option, scissors_option]
    emojis: list[str] = ["👊", "✋", "✌️"]
    opponent_choice: int = random.choice(valid_options)
    user_choice: int = int(input("Type the number: "))

    if user_choice not in valid_options:
        print("Wrong option!")
        return

    print(f"Your pick: {user_choice} - {emojis[user_choice - 1]}")
    print(f"Opponent's pick: {opponent_choice} - {emojis[opponent_choice - 1]}")

    if user_choice == opponent_choice:
        print("😡 It's a tie! 😡")
    elif ((user_choice == rock_option and opponent_choice == scissors_option)
          or (user_choice == paper_option and opponent_choice == rock_option)
          or (user_choice == scissors_option and opponent_choice == paper_option)):
        print("🎉 Hooray, you won! 🎉")
    else:
        print("😭 You lost! 😭")


if __name__ == '__main__':
    main()
