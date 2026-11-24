import requests
import endpoint
from logger import logger


def get_advanced_course(header):
    logger.info("Starting advanced course retrieval")

    for attempt in range(10):
        try:
            get_course_response = requests.get(endpoint.get_adv_courses_endpoint, headers=header)
            if get_course_response.status_code == 200:
                logger.info("Advanced courses retrieved successfully")
                print("Advanced courses retrieved successfully.")
                print(get_course_response.json())
                return get_course_response.json()
            else:
                logger.warning(
                    "Attempt %s failed. Status code: %s",
                    attempt + 1,
                    get_course_response.status_code
                )
                logger.error("Response: %s", get_course_response.text)

        except requests.RequestException:
            logger.exception(
                "Attempt %s: Get advanced courses request failed", attempt + 1
            )

            print(f"Attempt {attempt + 1}: Failed to retrieve courses. Retrying...")

    return None