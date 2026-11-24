import register as reg
import data
import login
import add_course
import get_adv_course as adv
import delete_course as dc

username, password = reg.test_register_user()
my_header = login.test_login_user(username, password)
course_id = add_course.add_advance_course(my_header)
courses = adv.get_advanced_course(my_header)
dc.delete_courses(my_header, course_id)
