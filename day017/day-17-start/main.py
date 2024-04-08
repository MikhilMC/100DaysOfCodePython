class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, other):
        other.following += 1
        self.followers += 1


# user_1 = User()
user_1 = User("001", "Angela")
# user_1.id = "001"
# user_1.username = "Angela"


user_2 = User("002", "Jack")
# user_2.id = "002"
# user_2.name = "Jack"

user_1.follow(user_2)
print(user_1.followers)
print(user_2.following)
