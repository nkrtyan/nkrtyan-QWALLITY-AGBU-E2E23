import requests
import endpoints
import data
import logging

def test_delete_course(course_id, headers):
    for attempt in range(10):
        try:
            delete_response = requests.delete(
                endpoints.delete_course_endpoint % course_id,
                headers=headers
            )
                   
            #TODO id admin role_id/#FIXED
            role_id = int(data.register_body.get("role_id", 2))

            if role_id == 2 and delete_response.status_code in (401, 403):
                logging.info(f"Verified: Delete request was denied as expected because Non-admin user should NOT be able to delete a course! Status code: {delete_response.status_code}")
                return True
            elif role_id == 2 and delete_response.status_code == 200:
                logging.error(f"BUG WARNING: Non-admin user was able to delete the course! Status code: {delete_response.status_code}")
                return False
            elif role_id == 1 and delete_response.status_code == 200:
                logging.info(f"Verified: Admin user deleted the course successfully! Status code: {delete_response.status_code}")
                return True
            elif delete_response.status_code == 404:
                logging.error(f"Error 404: Course with ID {course_id} was not found!")
                return False
            else:
                logging.error(f"Attempt {attempt + 1}: Unexpected status code {delete_response.status_code}")

        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.error(f"Attempt {attempt + 1}: Delete request failed. Retrying...")
            
    return False

if __name__ == "__main__":
    test_delete_course()