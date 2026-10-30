import json


def load_users(filepath="users.json"):
    with open(filepath, "r") as file:
        return json.load(file)


def filter_users_by_name(users, name):
    filtered_users = [user for user in users if user.get("name", "").lower() == name.lower()]
    for user in filtered_users:
        print(user)


def filter_users_by_age(users, age):
    filtered_users = [user for user in users if user.get("age") == age]
    for user in filtered_users:
        print(user)


def filter_users_by_email(users, email):
    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]
    for user in filtered_users:
        print(user)


def main():
    users = load_users()
    filter_option = input("What would you like to filter by? ('name', 'age', 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(users, name_to_search)

    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_users_by_age(users, age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(users, email_to_search)

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()



