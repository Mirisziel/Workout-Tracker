# Importing important libraries
import requests
import datetime as dt
import os

# Fetching Current Date and Time
Date = (dt.datetime.today())
formatted_date = Date.strftime('%d/%m/%Y')
formatted_time = Date.strftime("%H:%M:%S")

# Variables
AUTH_TOKEN = os.environ.get("AUTH_BEARER")
APP_ID = os.environ.get("EXERCISE_APP_ID")
API_KEY = os.environ.get("API_KEY")
Exercise_Endpoint = os.environ.get("EXERCISE_ENDPOINT")
googleSheet_endpoint = os.environ.get("GOOGLESHEET_ENDPOINT")
gender = "Male"
weight_kg = "60"
height = "175.4"
age = "20"

# Input
exercise_input = input("What you did today?: ")

# Headers and Parameters
header1 = {
    "authorization": AUTH_TOKEN
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params_nlp = {
    "query": exercise_input,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height,
    "age": age
}

# Using NLP Through API
response = requests.post(url=Exercise_Endpoint, json=params_nlp, headers=header)
i = (len(response.json()["exercises"]))


# Filling Google Sheet Form
for x in range(i):
    Exercise = str(response.json()["exercises"][x]["name"])
    Duration = response.json()["exercises"][x]["duration_min"]
    Calories = response.json()["exercises"][x]["nf_calories"]
    params_sheet = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": Exercise.title(),
            "duration": Duration,
            "calories": Calories
        }
    }
    response2 = requests.post(url=googleSheet_endpoint, json=params_sheet, headers=header1)
    response2.json()


# GOOGLE SHEET LINK: https://docs.google.com/spreadsheets/d/10PdKB_xxO2Nd7bo-SUL95FIpE_UKhta_URV6ka02PLI/edit#gid=0
