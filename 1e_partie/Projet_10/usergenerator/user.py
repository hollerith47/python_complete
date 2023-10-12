"""Module to generate random users"""
import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR/"user.log", level=logging.DEBUG)

fake = faker.Faker(locale="ru-RU")

def get_user():
    """Generate a single user

    Returns:
        str: user
    """
    logging.info("Generating user.")
    # return F"{fake.first_name()} {fake.last_name()}"
    return F"{fake.email()}"

def get_users(n):
    """Generate a list of users

    Args:
        n (int): Number of user to generate

    Returns:
        list[str]: users
    """
    logging.info(f"Generating a list of {n} user{'s' if n>1 else ''}.")
    return [get_user() for _ in range(n)]
    '''autre methode sans comprehension des listes
    users=[]
    for _ in range(n):
        users.append(get_user())
    return users
    '''

if __name__ == "__main__":
    user= get_users(n=5)
    print(user)
