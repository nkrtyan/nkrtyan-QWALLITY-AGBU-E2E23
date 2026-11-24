import requests as r
import data as d
import endpoints as e


def test_login_user(username, password):

    login_body = {
        "username": username, 
        "password": password
    }

    try:
        login_user_response = r.post(
            e.login_endpoint, 
            headers=d.headers, 
            json=login_body, 
            timeout=30
        )

        print("Login Status Code:", login_user_response.status_code)
        print("Login Response:", login_user_response.text)

        if login_user_response.status_code == 200:
            print("Login successful!")
            return True

        else:
            print("Login failed!")
            return False

    except r.exceptions.RequestException as error:
        print("Login request error:", error)
        return False
