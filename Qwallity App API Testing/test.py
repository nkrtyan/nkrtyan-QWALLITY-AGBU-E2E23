import register_user
import login 
import add_course
import get_advanced_course
import delete_course
import account_balance
import get_account_balance


username, password = register_user.test_register_user()
non_admin_header = login.test_login_user(username,password)
course_id = add_course.test_add_course(headers = non_admin_header)
get_advanced_course.test_get_advanced_courses(course_id = course_id, headers = non_admin_header)
delete_course.test_delete_course(course_id = course_id, headers = non_admin_header)
account_balance.test_adding_account_balance(headers = non_admin_header)
get_account_balance.test_get_account_balance(headers = non_admin_header)

print("Test scenarion is finished successfully!")