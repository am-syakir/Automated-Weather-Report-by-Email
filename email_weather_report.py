# Import required library
import requests
import smtplib


# Use requests lib to pull the current weather
## city name example: Kuala Lumpur, London, New York
Key_API = "{openweathermap_API_key}"
current_weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={your_city_name}&appid={Key_API}&units=metric")


# Convert the response as dict and select required weather parameters
## rain parameter is only available in data if it is raining or just rained
## units: Celcius for temperature, meter/sec for wind speed, and mm for rain volume
response = current_weather_response.json()

weather = response["weather"][0]["description"]
temperature = response["main"]["temp"]
humidity = response["main"]["humidity"]
feels_like = response["main"]["feels_like"]
wind_speed = response["wind"]["speed"]
rain1h = response.get("rain", {}).get("1h", 0)
rain3h = response.get("rain", {}).get("3h", 0)


# Set up the SMTP connection with Gmail
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()

conn.login('{sender_email}', '{sender_16_key_google_app_password}')


# Loop for sending the emails one by one with formatted message
email_list = ['{email_1}', '{email_2}', '{email_3}', '{email_4}']

for email in email_list:
    sender = '{sender_email}'
    receivers = email

    message = ("From: {sender_name} <{sender_email}>\n" +
               "To:" + email.split('@')[0] + "<" + email + ">\n" +
               "Subject: Today's Weather Report\n" +
               "TODAY'S WEATHER\n" +
               "===============\n" +
               f"Weather: {weather}\n" +
               f"Temperature: {temperature} 'C\n" +
               f"Humidity: {humidity}%\n" +
               f"Feels like: {feels_like} 'C\n" +
               f"Wind Speed: {wind_speed} meter/sec\n" +
               f"Rain volume last 1 hour: {rain1h} mm\n" +
               f"Rain volume last 3 hours: {rain3h} mm")

    conn.sendmail(sender, receivers, message)
