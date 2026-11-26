import requests
import endpoints

def test_delete_course(courese_id, headers):
    try:

        delete_course_request = requests.delete(endpoints.delete_course_endpoint%courese_id, headers= headers)
        if delete_course_request:
            print(f'{courese_id} Deleted')
            print(delete_course_request.text)
        else:
            print ('Delete Error')

    except requests.RequestException as e:
        print(e)