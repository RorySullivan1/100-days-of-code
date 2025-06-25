# Instagram Example
#
class User:

    def __init__(self, id: str, username: str):
        self.id = id
        self.username = username
        self.follower: int = 0
        self.following: int = 0
        ...

    def add_follower(self):
        self.follower += 1
        ...

    def follow_user(self, user):
        user.follower += 1
        self.following += 1
        ...
#
user_1 = User("001", "James")
user_2 = User("002", "Alex")

print(user_2.follower)
print(user_1.following)
user_1.follow_user(user_2)
print(user_2.follower)
print(user_1.following)
