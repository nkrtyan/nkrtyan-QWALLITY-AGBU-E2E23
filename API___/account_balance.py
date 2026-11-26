import requests
import endpoints


def excisting_balance(headers):
     for attempt in range(5):
            try:
                exist_balance_response = requests.get(endpoints.account_balance_endpoint, headers=headers)
                
                if exist_balance_response.status_code == 200:
                    balance = exist_balance_response.json().get("balance")
                    return balance
                else:
                    print(f"Getting balance failed.")

            except (requests.RequestException, ValueError) as e:
                print(e)
                print(f"Attempt {attempt + 1}: Balance adding failed. Retrying...")
                
                
     return None
 
                