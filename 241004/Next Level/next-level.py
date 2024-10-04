class User:
    def __init__(self, user_id, level):
        self.user_id = user_id
        self.level = level

    def display_info(self):
        print(f"user {self.user_id} lv {self.level}")

user1 = User("codetree", 10)

input_user_id, input_level = input().split()
input_level = int(input_level)

user2 = User(input_user_id, input_level)

user1.display_info()
user2.display_info()