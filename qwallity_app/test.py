import register_user
import login


new_username, new_password = register_user.test_register_user()
login.test_login_user(new_username,new_password)
print("Test scenario is finished successfully!")