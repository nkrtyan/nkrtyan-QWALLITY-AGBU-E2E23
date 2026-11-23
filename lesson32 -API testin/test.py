import register_user
import login
import add_course
import get_foundamental_courses
import delete_course


register_user.test_register_user()
header =login.test_login_user()
course_id =add_course.test_add_coures(headers=header)
get_foundamental_courses.test_get_found_coures(course_id=course_id, headers=header)
delete_course.test_delete_course(course_id=course_id, headers=header)
print("Test sqenario is finished successfully")
