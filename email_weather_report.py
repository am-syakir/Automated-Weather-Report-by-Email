# Import required library
import requests
import smtplib


# Use requests lib to pull the current weather
Key_API = "e760a014ff45365443a294b151a7368a"
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

conn.login('amsyakir@gmail.com', 'pxuipvknosybqgqr')


# Loop for sending the emails one by one with formatted message
email_list = ['eloncook31@gmail.com', 'stevezuckerberg2018@gmail.com', 'jeffcookdata@gmail.com', 'amsyakir@gmail.com']

for email in email_list:
    sender = 'amsyakir@gmail.com'
    receivers = email

    message = ("From: Amirul Syakirin <amsyakir@gmail.com>\n" +
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