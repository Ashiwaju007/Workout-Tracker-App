
import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "65"
HEIGHT_CM = "1.67"
AGE = "33"

APP_ID ="ID"
API_KEY = "API KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/4e9f7ba77ccaa3eb323263334dce60e7/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Read Excercise and Save to google sheet ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headersAPI = {
                'accept': 'application/json',
                'Authorization': 'Bearer ' + 'Password',
            }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headersAPI)
    print(sheet_response.text)
