import endpoints
import data
import requests


def test_register_user():
    register_data =data.register_body

    for attemt in range(10)
    try:
        register_user_response = request.post(endpoints.register_endpoint, json=register_data, headers=data.hesders)

        if data.register_user_response.status_code==201
        username =register_data['username']
        password = register_data['password']
        