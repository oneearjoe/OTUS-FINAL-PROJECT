from faker import Faker
import random

fake = Faker()

def generate_user_data():
    return {
        "name": fake.first_name(),
        "email": fake.email(),
        "password": "Test123!",
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "address": fake.address().replace("\n", " "),
        "country": random.choice(["Canada", "United States", "Australia"]),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile": fake.phone_number()
    }