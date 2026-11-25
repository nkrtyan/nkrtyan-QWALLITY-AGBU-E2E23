import requests
import endpoints
import data
import logging

def test_register_user():
    register_data = data.register_body
    
    for attempt in range(10):
        try:
            register_user_response = requests.post(
                endpoints.register_endpoint, 
                json=register_data, 
                headers=data.headers
            )
            
            if register_user_response.status_code == 201:
                username = register_data["username"]
                password = register_data["password"]
                logging.info(register_user_response.json())
                logging.info("User registered successfully!")
                logging.info("Username: ", username)
                logging.info("Password: ", password)
                return username, password
            else:
                logging.error(f"The registration is failed with this status code:", register_user_response.status_code)
                logging.error("Response: ", register_user_response.text)

        except requests.exceptions.RequestException as e:
            logging.error(f"Attempt {attempt + 1} Registrfailed. Retrying...")

if __name__ == "__main__":
    test_register_user()