import endpoints
import requests
import data

def test_get_account_balance(headers):
    for attempt in range(10):

        try:
            get_account_balance_response = requests.get(endpoints.get_account_balance_endpoint, headers=headers)

            if get_account_balance_response.status_code == 200:
                new_balance = int(get_account_balance_response.json().get("balance"))
                print(new_balance)
                break
            else:
                print(f"Error while trying get account balance")
                break

        except requests.RequestException as e:
            print(e) 
            print(f"Attempt {attempt + 1}: Getting account balance failed. Retrying... ")    


if __name__ == "__main__":
    test_get_account_balance(data.headers)             