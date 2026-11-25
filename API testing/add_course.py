import requests
import endpoints
import data
import logging

def test_add_course(headers):
    for attempt in range(10):
        try:
            add_course_response = requests.post(
                endpoints.add_course_endpoint, 
                json=data.course_body,
                headers=headers
            )
            course_id = add_course_response.json().get("id")
            role_id = int(data.register_body.get("role_id", 2))

            #TODO id admin role_id/#FIXED
            if role_id == 1 and course_id:
                logging.info(f"New course with this {course_id} id is added successfully!")
                break
            elif role_id == 2 and add_course_response.status_code in (200, 201):
                logging.error("BUG WARNING: Non-admin user should NOT be able to add a course!")
                break
            elif role_id == 2 and add_course_response.status_code in (401, 403):
                logging.info("Verified: Non-admin user was denied adding a course as expected!")
                break
            elif add_course_response.status_code == 404:
                logging.error("Error 404: Add course endpoint not found.")
                break
            else:
                logging.error(f"Attempt {attempt + 1}: Unexpected status code {add_course_response.status_code}")


        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.error(f"Attempt {attempt + 1}: Course adding failed. Retrying...")
    
    return course_id

if __name__ == "__main__":
    test_add_course()