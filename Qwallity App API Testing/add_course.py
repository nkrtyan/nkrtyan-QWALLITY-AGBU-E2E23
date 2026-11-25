import requests
import endpoints
import data
import logging

def test_add_course(headers):
    logging.info("Starting advanced course creation")

    role_id = data.register_body["role_id"]

    for attempt in range(10):
            try:
                  add_course_response = requests.post(endpoints.add_course_endpoint,json = data.course_body, headers=headers)

                  if add_course_response.status_code == 200:
                        course_id = add_course_response.json().get("id")

                        if role_id == 2 and add_course_response.status_code == 200:
                            logging.warning("Course %s added by Non-Admin user", course_id)
                            print(f"Course created by Non-Admin user. Course ID: {course_id}")
                            return course_id
                        
                        elif role_id == 1 and add_course_response.status_code == 200:
                            logging.info("Course %s added by Admin user", course_id)
                            print(f"Course created by Admin user. Course ID: {course_id}")
                            return course_id
                        
                        elif role_id == 2 and add_course_response.status_code != 200:
                            logging.info("Course hasn't been created as a non admin user,as expected", course_id)

                        elif role_id == 1 and add_course_response.status_code != 200: 
                             logging.warning("Course hasn'been added by Admin user.")

                        else: logging.error(f"Unknown error. Status code: {add_course_response.status_code}")
                                    
                  #FIX check when admin or non admin added course, info message,was authorized for ot or not ?

            except requests.RequestException as e:
                print(e)
                logging.info(f'Attempt{attempt + 1}: Add Course failed. Retrying... ')

    return course_id
               
                        