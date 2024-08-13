from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fall-detected', methods=['POST'])
def fall_detected():
	data = request.get_json()
	print("Fall detected! Triggering Alexa...")
	response = trigger_alexa_skill(data)
	return jsonify(response.json()), response.status_code

def trigger_alexa_skill(data):
	alexa_url = "http://localhost:3000/alexa-skill" #replace with your Alexa skill end point
	response = requests.post(alexa_url, json={"user_id": data['user_id']})
	return response

if __name__ == '__main__':
	app.run(port=5000)