import os
import json
import paho.mqtt.client as mqtt
from datetime import datetime
from weatherDataLib import WeatherGCodeWriter
import mqttConfig as mqtt_config

writer = WeatherGCodeWriter()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(mqtt_config.TOPIC)
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        dt = datetime.fromtimestamp(float(data.get("dateTime", 0)))
        entry = {
            "time": f"{dt.strftime('%H:00')}",
            "temp": float(data["outTemp_C"]),
            "humidity": float(data["outHumidity"]),
            "wind_high": float(data["windGust_kph"]),
            "rain": float(data["dayRain_cm"]),
            "eco2": writer.latest_eco2,
            "tvoc": writer.latest_tvoc
        }

        svg_file = writer.write_weather_data_to_svg([entry], svg_file_prefix="time_data")
        svg_filename_only = os.path.basename(svg_file)
        writer.svg_to_gcode(svg_filename_only, "test_weather.gcode")

        print("G-code generation successful")
        client.disconnect()

    except Exception as e:
        print("Error processing message:", e)
        client.disconnect()

client = mqtt.Client()
client.username_pw_set(mqtt_config.USERNAME, mqtt_config.PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to MQTT broker...")
client.connect(mqtt_config.BROKER, mqtt_config.PORT, 60)
client.loop_forever()