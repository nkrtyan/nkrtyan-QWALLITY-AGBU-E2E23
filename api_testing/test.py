import register_user
import login
import data


register_user.test_register_user()
header = login.test_login_user(data.register_body["username"], data.register_body["password"])
