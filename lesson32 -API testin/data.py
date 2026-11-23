from faker import Faker
fake = Faker()

headers ={
    'Content_Type': aplication/json

}
register_body ={
  "first_name": fake.first_name(),
  "email": fake.email(),
  "username": fake.user_name(),
  "password": fake.password(lenght=8),
  "role_id": 2,
  "account": fake.random_init(min=20,max=100)

}
course_body ={
  "title": "demo_cours",
  "body": "ademo_cours",
  "coursetype": "1",
  "author": "admin_user",
  "price": 100
}
