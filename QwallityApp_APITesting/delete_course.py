import data
import endpoint
import requests
import logging

logger = logging.getLogger(__name__)


def delete_courses(header, course_id):
    logger.info(f"Starting course deletion. Course ID: {course_id}")
    role_id = data.register_body["role_id"]
    author = data.course_body["author"]

    if role_id != 1 or author != "admin_user":
        logger.warning("Course deletion denied. User is not an admin.")
        return False

    for attempt in range(10):
        try:
            logger.info(f"Attempt {attempt + 1}: Deleting course {course_id}")
            delete_course_response = requests.delete(endpoint.delete_course_endpoint % course_id, headers=header)

            if delete_course_response.status_code == 200:
                logger.info(f"Course {course_id} deleted successfully.")
                logger.debug(delete_course_response.text)
                return True

            elif delete_course_response.status_code == 404:
                logger.warning(f"Course {course_id} not found.")
                return False

            elif delete_course_response.status_code == 401:
                logger.error("Unauthorized access. Please check your credentials.")
                return False

            else:
                logger.error(
                    f"Failed to delete course {course_id}. "
                    f"Status code: {delete_course_response.status_code}"
                )
                return False

        except requests.RequestException:
            logger.exception(
                f"Attempt {attempt + 1}: Deleting course failed. Retrying..."
            )
    return False
