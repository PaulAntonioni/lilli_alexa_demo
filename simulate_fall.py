import requests

data = {
    "user_id": "1234",
    "sensor_data": "motion detected, user inactive"
}

response = requests.post('http://localhost:5000/fall-detected', json=data)
print(response.json())
