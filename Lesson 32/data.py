from faker import Faker
fake = Faker()

headers = {
    "accept": "*/*", 
    "Content-Type": "application/json"
}

reg_body = {
    "first_name": fake.first_name(),
    "email": fake.unique.email(),
    "username": fake.unique.user_name(),
    "password": fake.password(length = 8),
    "role_id": 2,
    "account": fake.random_int(min = 20, max = 100),
}
