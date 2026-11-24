import data
import endpoint
import requests
from requests.auth import HTTPBasicAuth

def delete_courses(header, course_id):
    role_id = data.register_body["role_id"]
    
    for attempt in range(10):
        try:
            delete_course_response = requests.delete(endpoint.delete_course_endpoint%course_id, headers=header)
            if delete_course_response.status_code == 200 and role_id == 1:
                print(f"Course {course_id} deleted successfully. ")
                print(delete_course_response.text)
                return True
            elif delete_course_response.status_code == 200 and role_id == 2:
                print("You can't delete the course: only an admin can delete courses.")
                return False
            elif delete_course_response.status_code == 404:
                print(f"Course {course_id} not found. ")
                return False
            elif delete_course_response.status_code == 401:
                print(f"Unauthorized access. Please check your credentials. ")
                return False
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Deleteing course is failed. Retrying...")