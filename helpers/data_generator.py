from faker import Faker
import random

fake = Faker()

def generate_user_data():
    return {
        "name": fake.first_name(),                 
        "email": fake.email(),           
        "password": "123Qwe!!",                    
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "address": fake.address().replace("\n", " "),
        "country": random.choice(["Coruscant", "Tatooine", "Naboo"]),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile": fake.phone_number()
    }