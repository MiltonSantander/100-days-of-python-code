import requests
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))

parameters = {
    "lat": MY_LONG,
    "lng": MY_LAT,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


#Getting iss location

def get_iss_location():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


# If the ISS is close to my current position

def is_iss_close():
    iss_latitude, iss_longitude = get_iss_location()
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5:
        if MY_LONG + 5 >= iss_longitude >= MY_LAT - 5:
            return True
    return False


# and it is currently dark

def is_dark():
    if int((datetime.now()).strftime("%H")) >= sunset - 4:
        print("Ya es de nocheeee")
        return True
    return False


# Then send me an email to tell me to look up.

def send_email():
    print("mira el cielo!!!!")


# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_dark():
        if is_iss_close():
            send_email()
