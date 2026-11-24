from faker import Faker
fake = Faker()

headers = {
    "Content-type": "application/json", 
    "accept": "*/*"
}

register_body = {
    "first_name": fake.first_name(),
    "email": fake.email(),
    "username": fake.user_name(),
    "password": fake.password(length=8),
    "role_id": 1,
    "account": fake.random_int(min=20, max=100),
}

course_body = {
    "title": "demo_course",
    "body": "ademo_course",
    "coursetype": "1",
    "author": "admin_user",
    "price": 100,
}
