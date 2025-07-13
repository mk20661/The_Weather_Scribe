import os
import json
import time
import datetime
from weatherDataLib import WeatherGCodeWriter, send_gcode_to_arduino, paperRoll
import paho.mqtt.client as mqtt
import mqttConfig as mqtt_config

PORT = "/dev/ttyACM0"  # Adjust based on your device's actual serial port

writer = WeatherGCodeWriter()

mqtt_data_entry = None
mqtt_received = False

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("MQTT connected")
        client.subscribe(mqtt_config.TOPIC)
    else:
        print("MQTT connection failed with code:", rc)

def on_message(client, userdata, msg):
    global mqtt_data_entry, mqtt_received
    try:
        data = json.loads(msg.payload.decode())
        dt = datetime.datetime.fromtimestamp(float(data.get("dateTime", 0)))
        mqtt_data_entry = [{
            "time": dt.strftime("%H:00"),
            "temp": float(data["outTemp_C"]),
            "humidity": float(data["outHumidity"]),
            "wind_high": float(data["windGust_kph"]),
            "rain": float(data["dayRain_cm"]),
            "eco2": writer.latest_eco2,
            "pm25": writer.latest_pm25
        }]
        mqtt_received = True
        print("MQTT data received")
    except Exception as e:
        print("Failed to parse MQTT data:", e)

def init_header():
    run_hourly_task()
    print("Initializing header")
    paperRoll(stepSize=20, port=PORT)
    writer.write_header_to_svg()
    send_gcode_to_arduino("../gcodeOut/daily_report_header.gcode", port=PORT)
    paperRoll(stepSize=5, port=PORT)

    run_hourly_task()

def run_hourly_task():
    global mqtt_data_entry, mqtt_received
    mqtt_data_entry = None
    mqtt_received = False

    print("Waiting for MQTT data...")
    client = mqtt.Client()
    client.username_pw_set(mqtt_config.USERNAME, mqtt_config.PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqtt_config.BROKER, mqtt_config.PORT, 60)
    client.loop_start()

    timeout = 30
    while not mqtt_received and timeout > 0:
        time.sleep(1)
        timeout -= 1
    client.loop_stop()

    if mqtt_received and mqtt_data_entry:
        svg_path = writer.write_weather_data_to_svg(mqtt_data_entry)
        gcode_filename = f"hourly_{datetime.datetime.now().hour}.gcode"
        writer.svg_to_gcode(svg_file=os.path.basename(svg_path), gcode_file=gcode_filename)
        print("Waiting 5 seconds before sending G-code")
        time.sleep(5)
        send_gcode_to_arduino(gcode_filename, port=PORT)
    else:
        print("MQTT data not received")

def main_loop():
    print("Starting daily loop")
    init_header()
    last_hour = -1
    daily_reset_done = False

    while True:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute

        if minute == 0 and hour != last_hour:
            print(f"Hourly task triggered: {hour:02d}:00")
            run_hourly_task()
            last_hour = hour

        if hour == 23 and minute >= 40 and not daily_reset_done:
            print("23:50 reached, writing new header")
            init_header()
            daily_reset_done = True

        if hour == 0 and minute < 50:
            daily_reset_done = False

        time.sleep(30)

if __name__ == "__main__":
    main_loop()
