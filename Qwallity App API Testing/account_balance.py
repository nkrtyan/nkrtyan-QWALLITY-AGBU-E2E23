import endpoints
import requests
import data
import login

def test_adding_account_balance(headers):
    account_data = data.account_balance_body

    for attempt in range(10):

        try:
            account_balance_response = requests.post(endpoints.account_balance_endpoint, json = account_data, headers=headers)

            if account_balance_response.status_code == 200:
                amount = account_data["amount"]
                card_number = account_data["card_num"]  
                print(f"Account filled with amount {amount} from card {card_number}")
                break
            else:
                print("Failed to fill account balance. Status code:", account_balance_response.status_code)
                print("Response:", account_balance_response.text)
                break 


        except requests.RequestException as e:
            print(e) 
            print(f"Attempt {attempt + 1}: Filling account balance failed.Retrying... ")


if __name__ == "__main__":
    test_adding_account_balance(data.headers)
