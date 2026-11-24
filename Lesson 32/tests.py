import register as reg
import login as log

username, password = reg.test_register_user()
log.test_login_user(username, password)
