# Import required library
import requests
import smtplib


# Use requests lib to pull the current weather
Key_API = "{openweathermap API key}"
current_weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Kuala Lumpur&appid={Key_API}&units=metric")


# Convert the response as dict and select required weather parameters
## rain parameter is only available in data if it is raining or just rained
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

conn.login('{sender email}', '{16 key google app password}')


# Loop for sending the emails one by one with formatted message
email_list = ['{email 1}', '{email 2}', '{email 3}', '{email 4']

for email in email_list:
    sender = '{sender email}'
    receivers = email

    message = ("From: {sender name} <{sender email}>\n" +
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
