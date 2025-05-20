import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
choice = random.randint(0, len(friends))
friend_chosen = friends[choice]
print(friend_chosen)