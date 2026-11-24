import register_user
import login
import data
import add_course_adv
import delete_course
import get_balance
import add_balance



username, password = register_user.test_register_user()
my_header = login.test_login_user(username, password)
course_id = add_course_adv.add_advance_course(my_header)
added_balance = add_balance.add_account_balance(my_header)
delete_course.delete_courses(my_header, course_id)
