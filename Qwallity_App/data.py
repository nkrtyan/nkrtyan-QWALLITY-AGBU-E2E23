from faker import Faker
fake = Faker()

headers = {
    'Content-Type': 'application/json'
}

register_body = {
                "first_name": fake.first_name_female(),
                "email": fake.email(),
                "username": fake.user_name(),
                "password": fake.password(lenght=8),
                "role_id": 2,
                "account": fake.random_int(min=20, max=100)
                }

course_body = {
                "title": "Python_Basics",
                "body": "Introduction_to_Python",
                "coursetype": "1",
                "author": "admin_user",
                "price": 100
                }

