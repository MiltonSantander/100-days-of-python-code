import requests
import threading
from datetime import datetime

MY_LAT = -25.306812  # Your latitude
MY_LONG = -57.546178  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

print(data)

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print("sunset", data["results"])
print("hora local", (datetime.now()).strftime("%H"))


# If the ISS is close to my current position

def is_iss_close():
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5:
        if MY_LONG + 5 >= iss_longitude >= MY_LAT - 5:
            return True
    return False


# and it is currently dark

def is_dark():
    if int((datetime.now()).strftime("%H")) >= sunset - 4:
        print("esta oscuro")
        return True
    return False


# Then send me an email to tell me to look up.

def send_email():
    print("mira el cielo!!!!")


# BONUS: run the code every 60 seconds.

def loop():
    new_thread = threading.Timer(60.0, loop)
    new_thread.daemon = True
    new_thread.start()
    if is_dark():
        if is_iss_close():
            send_email()


loop()
