import requests as r
import data as d
import endpoints as e


def test_register_user():

    try:
        reg_user_response = r.post(
            e.register_endpoint, 
            headers=d.headers, 
            json=d.reg_body, 
            timeout=30
        ) 
        print("Register Status Code:", reg_user_response.status_code)
        print("Register Response:", reg_user_response.text)

        if reg_user_response.status_code == 201:
            print("User registered successfully!")
            username = d.reg_body["username"]
            password = d.reg_body["password"]
            return username, password
        else:
            print("Registration failed!")
            return None

    except r.exceptions.RequestException as error:
        print("Register request error:", error)
        return None


