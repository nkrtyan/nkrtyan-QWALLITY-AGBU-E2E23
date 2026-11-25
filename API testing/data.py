from faker import Faker
fake = Faker()

headers = {
    'Content-Type': 'application/json'
}

register_body = {
                "first_name": fake.first_name(),
                "email": fake.email(),
                "username": fake.user_name(),
                "password": fake.password(length=8),
                "role_id": 2,
                "account": fake.random_int(min=20, max=100)
                }

course_body = {
                "title": fake.name(),
                "body": fake.text(),
                "coursetype": "2",
                "author": fake.name(),
                "price": 100
                }

add_amount_body = {
                "amount": 100, 
                # fake.random_int(min=100, max=300),
                "payment": "2",
                "card_num": 0,
                "exp_date": "yyyy/mm/dd",
                "card_cvv": "string"
                }