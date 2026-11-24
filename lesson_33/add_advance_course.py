import requests
import endpoints
import data


def test_add_advance_course(headers):
    for attempt in range(10):
        try:
            add_course_response = requests.post(endpoints.add_course_endpoint, json=data.course_body, headers=headers)
            if add_course_response.status_code == 201:
                print("Course added successfully!")
                course_id = add_course_response.json().get("id")

                if course_id:
                    print(f"{course_id} Course added successfully.")
                    break 

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Course adding failed. Retrying...")


    return course_id
