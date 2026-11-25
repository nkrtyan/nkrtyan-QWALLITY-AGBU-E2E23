import requests
import endpoints
import data
import json
import logging

def test_get_advanced_courses(course_id, headers):
    logging.info("Starting advanced course retrieval")

    for attempt in range(10):

        try:
            get_advanced_course_response = requests.get(endpoints.get_adv_courses_endpoint,headers=headers)

            if get_advanced_course_response:
                logging.info("Advanced courses retrieved successfully")
                all_adv_courses = json.loads(get_advanced_course_response.text)

                for i in all_adv_courses["result"]:
                    if int(course_id) == i["id"]:
                        print(f"New added advanced course {course_id} exist in the list")
                        break
                break
            else:
                logging.warning(
                    "Attempt %s failed. Status code: %s",
                    attempt + 1,
                    get_advanced_course_response.status_code
                )
                logging.error("Response: %s", get_advanced_course_response.text)

        except requests.RequestException as e:
            print(e)
            logging.info(f"Attempt {attempt + 1}: Get advanced courses failed.Retrying... ")     


