from lesson_33 import add_account_balance
import register_user
import login
import add_advance_course
import get_account_balance
import delete_course


username, password = register_user.test_register_user()
header = login.test_login_user(username, password)
course_id = add_advance_course.test_add_advance_course(header)
balance = get_account_balance.test_get_account_balance(header)
added_balance = add_account_balance.test_add_account_balance(header)
delete_course = delete_course.test_delete_course(header, course_id)
print("Test scenario completed successfully. User registered and logged in.")