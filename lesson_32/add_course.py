import data
import endpoints
import requests

def test_add_course(headers):
    try:
        add_course_response = requests.post(endpoints.add_course_register_endpoint, json = data.course_body, headers=headers)
        course_id = add_course_response.json().get('id')
        if course_id:
            print(f'{course_id} Cousre added')
    except requests.RequestException as e:
        print(e)

    return course_id