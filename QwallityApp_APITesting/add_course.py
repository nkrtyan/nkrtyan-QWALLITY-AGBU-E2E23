import data
import endpoint
import requests
from logger import logger


def add_advance_course(header):
    logger.info("Starting advanced course creation")

    for attempt in range(10):
        try:
            add_course_response = requests.post(
                endpoint.add_course_endpoint, headers=header, json=data.course_body
            )

            if add_course_response.status_code == 200:
                course_id = add_course_response.json().get("id")

                if course_id:
                    logger.info("Course %s added successfully", course_id)
                    print(f"Course created successfully. Course ID: {course_id}")
                    return course_id

            logger.warning(
                "Attempt %s failed. Status code: %s",
                attempt + 1,
                add_course_response.status_code,
            )
            logger.error("Response: %s", add_course_response.text)

        except requests.RequestException:
            logger.exception("Attempt %s: Course creation failed", attempt + 1)
            print(f"Attempt {attempt + 1}: Course creation failed. Retrying...")

    return None
