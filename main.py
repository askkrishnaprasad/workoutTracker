import requests
from datetime import datetime

NUTRI_APP_ID = "****"
NUTRI_API_KEY = "****"
NUTRI_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = 72.5
HEIGHT = 170
AGE = 32
SHEETY_URL = "https://api.sheety.co/dff77407de861294b9de88feed4a3ce5/myWorkouts/workouts"

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
    "x-remote-user-id": "0"
}

exercise_data = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
today = datetime.now()
today_date = today.strftime("%Y/%m/%d")
today_time = today.strftime("%H:%M:%S")
response = requests.post(url=NUTRI_URL, json=exercise_data, headers=headers)
data_return = response.json()["exercises"]
print(data_return)
for data in data_return:
    workout_name = data["name"].title()
    workout_duration = data["duration_min"]
    workout_calory = data["nf_calories"]
    workouts = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": workout_name,
            "duration": workout_duration,
            "calories": workout_calory,
        }
    }
    response = requests.post(url=SHEETY_URL, json=workouts)
    print(response.text)

