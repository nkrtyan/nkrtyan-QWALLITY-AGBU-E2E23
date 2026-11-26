import register_user
import login
import add_course
import get_advenced_courses
import delete_course
import add_balance
import account_balance


username, password = register_user.test_register_user()
print(username, password)
header = login.test_login_user(username,password)

course_id = add_course.test_add_course(headers = header)

get_advenced_courses.test_get_adv_courses(course_id=course_id, headers=header)
delete_course.test_delete_course(course_id=course_id, headers = header)

balance = account_balance.excisting_balance(headers=header)
print("Account balance:", balance)

updated_balance = account_balance.excisting_balance(headers=header)

print("Updated balance:", updated_balance)

existing_balance = account_balance.excisting_balance(headers =header)
print(existing_balance)

added_balance = add_balance.test_add_balance(headers = header,existing_balance = existing_balance)
print(f"added balance is {added_balance}")



