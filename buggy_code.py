
def divide(a, b):
    return a / b  # Bug: crashes when b is 0


def get_user_name(user):
    return user["name"]  # Bug: crashes if "name" is missing


def calculate_average(numbers):
    return sum(numbers) / len(numbers)  # Bug: crashes on an empty list


def get_discount(price, discount):
    return price - discount  # Bug: discount may exceed price


def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
def divide_by_zero_test():
    return 10 / 0
