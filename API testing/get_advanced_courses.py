import requests
import endpoints
import logging

def test_get_advanced_courses(course_id, headers):
    for attempt in range(10):
        try:
            response = requests.get(
                endpoints.get_advanced_courses_endpoint,
                headers=headers
            )
            
            if response.status_code == 200:
                if str(course_id) in response.text:
                    logging.info(f"Verified: Course with this {course_id} ID is in the list!")
                    return True
                else:
                    logging.error(f"Course with this {course_id} ID was NOT found in the advanced courses list!")
                    return False
            else:
                logging.error(f"Attempt {attempt + 1}: Failed to get courses. Status code: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.error(f"Attempt {attempt + 1}: Request failed. Retrying...")
        
if __name__ == "__main__":
    test_get_advanced_courses()