import endpoints
import requests
import json


def test_get_fundamental_course(course_id, headers):
    try:
        get_fundamental_course_request = requests.get(endpoints.get_fund_courses_register_endpoint, headers=headers)
        if get_fundamental_course_request:
            all_fund_course = json.loads(get_fundamental_course_request.text)
            print(all_fund_course)

            for i in all_fund_course['result']:
                if int(course_id) == i['id']:
                    print('New course is in list')


    except requests.RequestException as e:
        print(e)