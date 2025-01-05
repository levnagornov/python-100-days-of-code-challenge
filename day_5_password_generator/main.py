import random
import string


def main() -> None:
    print("Welcome to my simple password generator!")

    letters: str = string.ascii_letters
    digits: str = string.digits
    punctuation: str = string.punctuation

    letters_number: int = int(input("How many letters do you want to have? "))
    digits_number: int = int(input("How many digits do you want to have? "))
    punctuation_number: int = int(input("How many punctuation symbols do you want to have? "))

    password: list[str] = []

    if letters_number > 0:
        password += random.sample(letters, letters_number)
    if digits_number > 0:
        password += random.sample(digits, digits_number)
    if punctuation_number > 0:
        password += random.sample(punctuation, punctuation_number)

    random.shuffle(password)

    print(f"Generated password of length {len(password)}:")
    print("".join(password))


if __name__ == '__main__':
    main()
