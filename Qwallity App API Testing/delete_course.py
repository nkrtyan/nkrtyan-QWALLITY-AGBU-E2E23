import requests
import endpoints

def test_delete_course(course_id, headers):
    for attempt in range(10):

        try:
            delete_course_response = requests.delete(endpoints.delete_course_endpoint%course_id, headers=headers)

            if delete_course_response:
                print(delete_course_response.status_code)
                print(f"Course {course_id} deleted successfully.")
                print(delete_course_response.text)
                break

        except requests.RequestException:
            print(f"Attempt {attempt + 1}: Course deletion failed. Retrying... ")

