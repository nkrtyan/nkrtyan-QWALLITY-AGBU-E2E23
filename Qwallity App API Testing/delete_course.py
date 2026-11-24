import requests
import endpoints

def test_delete_course(course_id, headers):
    for attempt in range(10):

        try:
            delete_course_response = requests.delete(endpoints.delete_course_endpoint%course_id, headers=headers)

            if delete_course_response.status_code == 401:
                print(f"Course deletion failed. Status code: {delete_course_response.status_code}")
                print(delete_course_response.text)
                break

            elif delete_course_response.status_code == 200:
                print(f"Course {course_id} deleted successfully.")
                break

            else:
                print(f"Unexpected response. Status code: {delete_course_response.status_code}")

        except requests.RequestException:
            print(f"Attempt {attempt + 1}: Course deletion failed. Retrying... ")         

