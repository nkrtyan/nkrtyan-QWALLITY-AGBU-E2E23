# lesson 32/lesson33

import register_user
import login
import add_course
import delete_course
import get_fundametal_course

username, password = register_user.test_register_user()
headers = login.test_login_user(username, password)
courese_id = add_course.test_add_course(headers)
get_fundametal_course.test_get_fundamental_course(courese_id, headers)
delete_course.test_delete_course(courese_id, headers)


