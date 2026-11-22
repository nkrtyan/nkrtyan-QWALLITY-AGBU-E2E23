import requests
import endpoints
import data

def test_add_course(headers):
    for attempt in range(10):
            
            try:
                  add_course_response = requests.post(endpoints.add_course_endpoint,json = data.course_body, headers=headers)

                  if add_course_response.status_code == 200:
                        course_id = add_course_response.json().get("id")
                        print(course_id)
                        break
                  
            except requests.RequestException as e:
                print(e)
                print(f'Attempt{attempt + 1}: Add Course failed. Retrying... ')

    return course_id

if __name__ == "__main__":
    test_add_course()                
                        