import data
import requests
from requests.auth import HTTPBasicAuth
import endpoints


def test_login_user(username,password):
    for attempt in range(1):
        
        try:
            login_response = requests.post(endpoints.login_endpoint, auth = HTTPBasicAuth(username, password))
            print("Status code:", login_response.status_code)
            print("Response:", login_response.text)
            print("Content-Type:", login_response.headers.get('Content-Type'))
            
            # if login_response.status_code == 200:
            token = login_response.json().get('token')
            
            print("Status code:", login_response.status_code)
            print("Response:", login_response.text)         
                        
            if  token:
                print("Login successful.")
                data.headers['Authorization'] = f'Bearer {token}'
                print(data.headers)
                break
               
        except requests.exceptions.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Login failed. Retrying  ")
            
    return data.headers
    
    
if __name__ == "__main__":
 
    test_login_user(
    data.register_body["username"],
    data.register_body["password"],
    
)
    


    
    
