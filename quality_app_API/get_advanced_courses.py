import endpoints
import json
import requests
import data

def test_get_adv_courses(course_id, headers):

 for attempt in range(7):
    
  try:
        get_adv_courses_response = requests.get(endpoints.get_adv_courses_endpoint, headers=headers)
        
        
        if get_adv_courses_response:
            all_adv_courses = json.loads(get_adv_courses_response.text)
            
            for i in all_adv_courses["result"]:
                if int(course_id) == i["id"]:
                    print(f'New added adv_course exists in list.')
                    print(i["id"])
                    break
  except requests.RequestException as e:
        print(f"Attempt {attempt + 1}: Login failed. Retrying....")



if __name__ == "__main__":
    adv = test_get_adv_courses(3, data.headers)
    print(adv)
