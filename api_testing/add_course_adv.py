import data
import endpoint
import requests
from requests.auth import HTTPBasicAuth

def add_advance_course(header):
    for attempt in range(10):
        try:
            add_course_response = requests.post(endpoint.add_course_endpoint, headers=header, json = data.course_body)
            if add_course_response.status_code == 200:
                course_id = add_course_response.json().get("id")
                
                if course_id:
                    print(f"Course {course_id} added successfully. ")   
            return course_id
                
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Course is deleted. Retrying...")
#TODO checking for non admin