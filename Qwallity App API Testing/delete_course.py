import requests
import endpoints
import logging
import data

def test_delete_course(course_id, headers):
    logging.info(f"Starting course deletion. Course ID: {course_id}")
    role_id = data.register_body["role_id"]
    author = data.course_body["author"]

    if role_id != 1 or author != "admin_user":
        logging.warning("Course deletion denied. User is not an admin.")
        return False

    for attempt in range(10):
        try:
            delete_course_response = requests.delete(endpoints.delete_course_endpoint%course_id, headers=headers)

# FIX checking for admin user , positive and negative cases

            if delete_course_response.status_code == 401 and role_id == 2:
                logging.info(f"Course deletion failed.Non admin can't delete course. Status code: {delete_course_response.status_code}")
                logging.info(delete_course_response.text)
                return True
    
            elif delete_course_response.status_code == 200 and role_id == 1:
                logging.info(f"Course {course_id} deleted successfully by Admin user.")
                return True

            elif delete_course_response.status_code == 200 and role_id == 2:
                logging.warning(f"Course was deleted by non Admin user. Bug!!!")  
                return False  

            else:
                logging.info(f"Unexpected response. Status code: {delete_course_response.status_code}")

        except requests.RequestException:
            logging.info(f"Attempt {attempt + 1}: Course deletion failed. Retrying... ")         

