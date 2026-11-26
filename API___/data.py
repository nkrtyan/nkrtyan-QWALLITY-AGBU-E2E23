from faker import Faker
fake = Faker()

headers = {
    'Content-type': 'application/json'
    
  
}

register_body = {
                "first_name": fake.first_name(),
                "email": fake.email(),
                "username": fake.user_name(),
                "password": fake.password(length=8),
                "role_id": 2,
                "account": fake.random_int(min=20, max = 100)
                }

course_body = {
                "title": "demo_course",
                "body": "ademo_course",
                "coursetype": "2",
                "author": "non_admin_user",
                "price": 100
                }

role_id_body = {
                "role_id": "1"
                }

add_balance_body = {
                    "amount": 50,
                    "payment": "2",
                    "card_num": 455659876543,
                    "exp_date": "2026/10/05",
                    "card_cvv": "123",
                    "author": "admin_user",
                }



