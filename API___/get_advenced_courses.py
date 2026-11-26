import endpoints
import json
import requests


def test_get_adv_courses(course_id, headers):
    
    for attempt in range(3):
        
        try:
            get_adv_courses_response = requests.get(endpoints.get_adv_courses_endpoint, headers=headers)
            
            if get_adv_courses_response: #status code checking
             
                  all_adv_courses = json.loads(get_adv_courses_response.text)
                  
                  for i in all_adv_courses["result"]:    
                      
                      if int(course_id) == int(i["id"]):
                          print(f'New added adv_course exists in list.')
                          print(f"get_ID is {i["id"]}")
                          break
                
                  break
        
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}: Login failed. Retrying....")
        









            
            
# if __name__ == "__main__":
 
   

        









# if __name__ == "__main__":
#     adv = test_get_adv_courses(3, data.headers)
    
#     print(adv)

    
    # test_get_adv_courses(3, data.headers)
    # print( test_get_adv_courses(3, data.headers))
    # test_get_adv_courses(3, "new123456")
    # print(test_get_adv_courses(3, "new123456"))


   # print("Headers:", headers)
            # print("Headers type:", type(headers))
            # print("Status code:", get_adv_courses_response.status_code)
            # print("Response:", get_adv_courses_response.text)
    