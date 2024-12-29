# This app is a simple band name generator.
# It will ask for a city name and a pet name, then it combines these two together.

def main() -> None:
    print("Welcome to the Band Name Generator!")
    city_name: str = input("What's the name of the city you grep up in?\n")
    pet_name: str = input("What's your pet's name?\n")
    print("Your band name could be", city_name, pet_name)

if __name__ == '__main__':
    main()
