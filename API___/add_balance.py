import requests
import endpoints
import json
import data
import account_balance


def test_add_balance(headers,existing_balance):

    add_balance_count = 0 
    
       #admin,none admin , from out get 

    for attempt in range(5):
        try:
            print("Request body:", data.add_balance_body)
            
            add_balance_response = requests.post(endpoints.add_account_balance_endpoint,json=data.add_balance_body, headers=headers)
            
            print("Status code:", add_balance_response.status_code)
            print("Response:", add_balance_response.text)
            
            if add_balance_response.status_code == 200:
                if data.role_id_body == "1":
                    
                    add_balance_count = account_balance.excisting_balance(headers)
                
                         
                expected_balance = (int(data.add_balance_body["amount"]) + int(existing_balance))
                print(f"{add_balance_count} balance added successfully.")
                break
            else:
                print(f"{add_balance_count} balance adding failed.")
                break
                

        except (requests.RequestException, ValueError) as e:
            print(e)
            print(f"Attempt {attempt + 1}: Balance adding failed. Retrying...")

    return add_balance_count







