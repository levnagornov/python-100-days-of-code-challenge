# This app is a simple tip calculator
# It requires to enter some data and then calculates the split for each person to pay.

def main() -> None:
    print("Welcome to the tip calculator!")
    bill: float = float(input("What was the total bill? $"))
    if bill < 1:
        raise ValueError("Error. The bill amount can't be less than 1.")

    tip: int = int(input("How much tip would you like to give? 10, 12 or 15? "))
    if tip < 1:
        raise ValueError("Error. The tip amount can't be less than 1.")

    people_number: int = int(input("How many people to split the bill? "))
    if people_number < 1:
        raise ValueError("Error. The people number can't be less than 1.")

    bill_with_tip: float = bill * (1 + tip / 100)
    split_per_person: float = round(bill_with_tip / people_number, 2)
    print(f"Each person should pay ${split_per_person:.2f}")


if __name__ == '__main__':
    main()
