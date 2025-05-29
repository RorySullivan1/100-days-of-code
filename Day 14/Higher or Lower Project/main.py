from game_data import data
from art import logo, vs
from random import randint

def main():
    print(logo)
    print("Welcome to Higher or Lower!\nWe are playing with instagram followers!\nPick the more popular celebrity!\n\n")

    game_on = True

    # Generate Random Number
    first_item = generate_random_item()

    while game_on:
        show_item(first_item, show_value=True)
        print(vs)
        new_item = generate_random_item()
        show_item(new_item, show_value=False)

        user_choice = input(f"Does {first_item["name"]} have a higher (H) or lower (L) follower count?").lower()

        if user_choice == "l":
            if first_item["follower_count"] > new_item["follower_count"]:
                user_loss(first_item, new_item)
                game_on = False
            else:
                first_item = new_item
        elif user_choice == "h":
            if first_item["follower_count"] < new_item["follower_count"]:
                user_loss(first_item, new_item)
                game_on = False
        else:
            raise IOError(f"Incorrect input {user_choice}. Input should be 'H' or 'l'")

def user_win(item_1: dict, item_2: dict):
    print(f"You Win!\n"
          f"{item_1["name"]} has {item_1["follower_count"]} followers vs. "
          f"{item_2["name"]}'s {item_2["follower_count"]}")

def user_loss(item_1: dict, item_2: dict):
    print(f"You lose!\n"
          f"{item_1["name"]} has {item_1["follower_count"]} followers vs. "
          f"{item_2["name"]}'s {item_2["follower_count"]}")

def generate_random_item():
    return data.pop(randint(0, len(data) - 1))

def show_item(item: dict, show_value: bool = False):
    output = f"Celebrity: {item["name"]} ({item["description"]}) from {item["country"]}"
    output += f"\nFollower Count: {item["follower_count"]}" if show_value else ""

    print(output)


if __name__ == "__main__":
    main()