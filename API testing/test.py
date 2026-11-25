import register_user
import login
import add_course
import get_advanced_courses
import delete_course
import account_balance
from logger_config import info_logging
import logging

info_logging()

new_username, new_password = register_user.test_register_user()
header = login.test_login_user(new_username, new_password)
logging.info(f"You have successfully registered and logged into the system with this username: {new_username}")
course_id = add_course.test_add_course(headers=header)
get_advanced_courses.test_get_advanced_courses(course_id=course_id, headers=header)
delete_course.test_delete_course(headers=header, course_id=course_id)
account_balance.test_fill_balance(headers=header)