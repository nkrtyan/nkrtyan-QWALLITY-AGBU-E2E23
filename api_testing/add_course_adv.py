import data
import endpoint
import requests
from requests.auth import HTTPBasicAuth

def add_advance_course(header):
    role_id = data.register_body["role_id"]
    
    for attempt in range(10):
        try:
            add_course_response = requests.post(endpoint.add_course_endpoint, headers=header, json = data.course_body)
            if add_course_response.status_code == 200 and role_id == 1:
                course_id = add_course_response.json().get("id")
                
                if course_id:
                    print(f"Course {course_id} added successfully. ")   
                    return course_id   
            elif add_course_response.status_code == 200 and role_id == 2:
                print(f"Adding course is failed. You are not admin.  ") 
                return False
                   
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Course is deleted. Retrying...")
#TODO checking for non admin