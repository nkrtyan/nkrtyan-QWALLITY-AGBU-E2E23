import endpoints
import data
import requests
from requests.auth import HTTPBasicAuth

def test_delete_course(headers, course_id):
    role_id = data.register_body["role_id"]
    author = data.course_body["author"]

    for attempt in range(10):
        try:
            if role_id != 1:
                print(" Non-admin users can't delete courses.")
                return False
            
            delete_course_response = requests.delete(endpoints.delete_course_endpoint%course_id, headers=headers)
            if delete_course_response.status_code == 200:
                print(f"Course with ID {course_id} deleted successfully!")
            elif delete_course_response.status_code == 404:
                print(f"Course with ID {course_id} not found.") 
            else:
                print(f"Failed to delete course with ID {course_id}. Status code: {delete_course_response.status_code}")
                print("Response:", delete_course_response.text)    

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Deleting course failed. Retrying...")

    return delete_course_response.json().get("message")