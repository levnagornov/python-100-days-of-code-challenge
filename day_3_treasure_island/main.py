import json


def play_scene(scene_key: str, game_data: dict) -> str:
    scenes: dict = game_data["scenes"]
    current_scene: dict = scenes[scene_key]
    description: str = current_scene["description"]
    print(description)

    # Check if story has already finished
    choices: dict = current_scene["choices"]
    if not choices:
        print("The story ends here.")
        return ""

    # Print choices
    for i, value in enumerate(choices.values()):
        text: str = value["text"]
        keyword: str = value["keyword"]
        print(f"  {text} - type '{keyword}'")

    # Get user choice
    user_choice: str = input("Enter the desired option: ").lower()

    # Return next scene
    for key, value in choices.items():
        if value["keyword"] == user_choice:
            return value["next_scene"]

    print("You made a wrong decision and now you're lost.")
    return ""

def main() -> None:
    print("Welcome to the Treasure Island!")
    print("Your mission is to find the treasure by answering question.")
    with open("adventure.json", "r") as file:
        game_data = json.load(file)

    next_scene: str = game_data["start"]
    while next_scene:
        next_scene = play_scene(next_scene, game_data)


if __name__ == '__main__':
    main()
