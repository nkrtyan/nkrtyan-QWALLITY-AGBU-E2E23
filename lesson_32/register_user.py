import endpoints
import data
import requests

def test_register_user():
    register_data = data.register_body

    try:
        register_user_response = requests.post(endpoints.register_endpoint, json = register_data, headers= data.headers)
        if register_user_response.status_code == 201 or 200:
            username = register_data['username']
            password = register_data['password']
            print('Registration complete')
            return username, password
        
        else:
            print(f'Failed to register user. Status code: {register_user_response.status_code}')
            print(f'Response: {register_user_response.text}')
    except requests.RequestException as e:
        print(e)

# if __name__ == '__main__':
#     test_register_user()


    