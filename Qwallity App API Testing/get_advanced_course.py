import requests
import endpoints
import data
import json

def test_get_advanced_courses(course_id, headers):
    for attempt in range(10):

        try:
            get_advanced_course_response = requests.get(endpoints.get_adv_courses_endpoint,headers=headers)

            if get_advanced_course_response:
                all_adv_courses = json.loads(get_advanced_course_response.text)
                print(all_adv_courses)

                for i in all_adv_courses["result"]:
                    if int(course_id) == i["id"]:
                        print(f"New added advanced course {course_id} exist in the list")

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Get advanced courses failed.Retrying... ")     


if __name__ == "__main__":
    test_get_advanced_courses()

