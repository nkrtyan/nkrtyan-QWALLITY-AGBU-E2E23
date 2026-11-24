from faker import Faker
fake = Faker()

headers = {
    "Content-Type": "application/json",
}    

register_body = {
                "first_name": fake.first_name(),
                "email": fake.email(),
                "username": fake.user_name(),
                "password": fake.password(length = 8),
                "role_id": 2,
                "account": fake.random_int(min = 20,max = 100)
            }

course_body = {
                "title": fake.word(),
                "body": fake.text(),
                "coursetype": 1,
                "author": "admin_user",
                "price": 100
}

balance_body = {
                "amount": 100,
                "payment": 2,
                "exp_date": "yyyy/mm/dd",
                 "card_cvv": "string"
}