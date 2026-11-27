import register_user
import login
import add_course
import delete_course
import getting_course 
import get_advanced_courses


username,password = register_user.register_user()
print(username,password)
token = login.login_user()
course_id = add_course.create_course(token=token)
get_advanced_courses.get_fundamental_course(course_id, headers=token)
delete_course.delete_course(course_id, headers=token)
print("Test scenario is finished successfully!")