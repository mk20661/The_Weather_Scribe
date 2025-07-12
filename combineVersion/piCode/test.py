import time
from datetime import datetime
from weatherDataLib import WeatherGCodeWriter, send_gcode_to_arduino, paperRoll

writer = WeatherGCodeWriter()
SerialPort="/dev/ttyACM0"

def write_header():
    paperRoll(stepSize=20, port=SerialPort)
    writer.write_header_to_svg()
    send_gcode_to_arduino("daily_report_header.gcode",port=SerialPort)
    paperRoll(stepSize=5, port=SerialPort)

def process_hourly_task():
    import paho.mqtt.client as mqtt
    import mqttConfig as mqtt_config
    import json

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            client.subscribe(mqtt_config.TOPIC)
        else:
            print("Connection failed with code", rc)

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
                "pm25": writer.latest_pm25 
            }
            svg_file = writer.write_weather_data_to_svg([entry], svg_file_prefix="time_data")
            writer.svg_to_gcode(svg_file, "../hourly_data.gcode")
            time.sleep(5 * 60)
            send_gcode_to_arduino("hourly_data.gcode", port=SerialPort)
            client.disconnect()
        except Exception as e:
            print("MQTT msg error:", e)
            client.disconnect()

    client = mqtt.Client()
    client.username_pw_set(mqtt_config.USERNAME, mqtt_config.PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqtt_config.BROKER, mqtt_config.PORT, 60)
    client.loop_forever()

def main_loop():
    print("== Init ==")
    paperRoll(stepSize=20, port=SerialPort)
    writer.write_header_to_svg()
    send_gcode_to_arduino("daily_report_header.gcode", port=SerialPort)
    paperRoll(stepSize=5, port=SerialPort)

    while True:
        now = datetime.now()
        if now.minute == 0:
            print(f"Hourly job started at {now.strftime('%H:%M')}")
            process_hourly_task()

        elif now.hour == 23 and now.minute >= 0:
            print("23:00 reached. Waiting for 23:50...")
            while datetime.now().minute < 50:
                time.sleep(30)

            print("Advancing paper and writing header for new day")
            paperRoll(stepSize=20, port=SerialPort)
            writer.write_header_to_svg()
            send_gcode_to_arduino("daily_report_header.gcode", port=SerialPort)
            paperRoll(stepSize=5, port=SerialPort)

if __name__ == "__main__":
    main_loop()
