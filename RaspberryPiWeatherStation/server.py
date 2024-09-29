#!/usr/bin/env python
from flask import Flask, request
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
import threading

app = Flask(__name__)

# Initialize the RGBMatrix
optionen = RGBMatrixOptions()
optionen.rows = 32
optionen.cols = 64
matrix = RGBMatrix(options=optionen)

# Global variables to store data
indoor_data = {}
outdoor_data = {}
current_device = 'ESP32_indoor'
last_update_time = time.time()

@app.route('/data', methods=['POST'])
def receive_data():
    global current_device, last_update_time

    # Authenticate the request
    auth = request.authorization
    if not auth or not (auth.username == 'admin' and auth.password == '20Wetterstation24'):
        return "Unauthorized", 401

    device_id = request.form.get('device_id')
    temperature = request.form.get('temperature')
    pressure = request.form.get('pressure')
    humidity = request.form.get('humidity')
    lightvalue = request.form.get('lightvalue')

    # Determine if it might rain
    if float(humidity) > 80 and float(pressure) < 1009:
        rain_status = "Possible Rain"
    else:
        rain_status = "No Rain"

    # Determine if it is day or night
    if float(lightvalue) < 1000:
        day_night_status = "Day"
    else:
        day_night_status = "Night"

    # Store the data
    data = {
        'temperature': temperature,
        'pressure': pressure,
        'humidity': humidity,
        'rain_status': rain_status,
        'day_night_status': day_night_status
    }

    if device_id == 'ESP32_indoor':
        indoor_data.update(data)
    elif device_id == 'ESP32_outdoor':
        outdoor_data.update(data)

    # Update the display immediately after receiving data
    update_display()

    return "Data received", 200

# Function to update the display
def update_display():
    global current_device, last_update_time

    # Create a graphics context
    canvas = matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("../../../fonts/4x6.bdf")
    color = graphics.Color(255, 255, 255)

    # Get the current data
    data = indoor_data if current_device == 'ESP32_indoor' else outdoor_data

    # Display the data
    device_label = "Indoor" if current_device == 'ESP32_indoor' else "Outdoor"
    graphics.DrawText(canvas, font, 2,  6, color, f"Device: {device_label}")
    graphics.DrawText(canvas, font, 2, 12, color, f"{data.get('temperature', 'N/A')} °C")
    graphics.DrawText(canvas, font, 2, 18, color, f"{data.get('humidity', 'N/A')} %")
    graphics.DrawText(canvas, font, 2, 24, color, data.get('rain_status', 'N/A'))
    graphics.DrawText(canvas, font, 2, 30, color, data.get('day_night_status', 'N/A'))

    # Swap the canvas
    matrix.SwapOnVSync(canvas)

    # Switch the device every 30 seconds
    if time.time() - last_update_time >= 30:
        last_update_time = time.time()
        current_device = 'ESP32_outdoor' if current_device == 'ESP32_indoor' else 'ESP32_indoor'

    # Start the timer again
    threading.Timer(30, update_display).start()

# Start the timer when the program starts
update_display()

if __name__ == '__main__':
    app.run(host='192.168.2.192', port=5000)