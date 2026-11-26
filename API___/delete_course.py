import endpoints
import requests



def test_delete_course(course_id, headers):
    
    for attempt in range(10):
        try:
            del_course_response = requests.delete(endpoints.delete_course_endpoint%course_id, headers=headers)
            if del_course_response: #TODO role_id checking
                print(del_course_response.status_code)
                print(f"Course {course_id} deleted successfully.")
                print(del_course_response.text)
                break
            else:
                print("the request is denied.")
                break
            
        except requests.RequestException:
            print("Attempt (attempt 1): Login failed. Retrying...")