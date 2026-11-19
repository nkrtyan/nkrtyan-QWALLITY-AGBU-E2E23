import register_user
import login 
import add_course
import get_fundamental_courses
import delete_course


register_user.test_register_user()
header = login.test_login_user()
course_id = add_course.test_add_course(headers=header)
get_fundamental_courses.test_get_fund_courses(course_id=course_id, headers=header)
delete_course.test_delete_course(course_id=course_id, headers=header)
print("Test scenarion is finished successfully!")