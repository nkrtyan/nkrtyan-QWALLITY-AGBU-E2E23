from faker import Faker
fake = Faker()

headers = {
    'Content-Type': 'application/json'
}

register_body = {
  "first_name": fake.first_name(),
  "email": fake.email(),
  "username": fake.user_name(),
  "password": fake.password(),
  "role_id": 2,
  "account": fake.random_int(min=20, max=100)
}

course_body = {
  "title": "homework_course",
  "body": "homework32_course",
  "coursetype": "1",
  "author": "admin_user",
  "price": 150
}