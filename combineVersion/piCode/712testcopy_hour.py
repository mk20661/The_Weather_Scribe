import os
import json
import time
import datetime
from weatherDataLib import WeatherGCodeWriter, send_gcode_to_arduino, paperRoll
import paho.mqtt.client as mqtt
import mqttConfig as mqtt_config

PORT = "/dev/ttyUSB0"  # 根据你的设备实际串口修改

writer = WeatherGCodeWriter()

mqtt_data_entry = None
mqtt_received = False

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ MQTT连接成功")
        client.subscribe(mqtt_config.TOPIC)
    else:
        print("❌ MQTT连接失败，错误码:", rc)

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
        print("✅ 收到 MQTT 数据")
    except Exception as e:
        print("❌ 解析 MQTT 数据失败:", e)

def init_header():
    print("🔁 初始化写入 Header")
    paperRoll(stepSize=20, port=PORT)
    writer.write_header_to_svg()
    send_gcode_to_arduino("daily_report_header.gcode", port=PORT)
    paperRoll(stepSize=5, port=PORT)

def run_hourly_task():
    global mqtt_data_entry, mqtt_received
    mqtt_data_entry = None
    mqtt_received = False

    print("🕐 等待 MQTT 数据...")
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
        print("⌛ 等待 5 秒（代替 5 分钟）")
        time.sleep(5)
        send_gcode_to_arduino(gcode_filename, port=PORT)
    else:
        print("⚠️ 未获取到 MQTT 数据")

def main_loop():
    print("🌞 启动每日循环")
    init_header()
    last_hour = -1
    daily_reset_done = False

    while True:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute

        # 整点触发（只触发一次）
        if minute == 0 and hour != last_hour:
            print(f"\n🕛 整点任务触发：{hour:02d}:00")
            run_hourly_task()
            last_hour = hour

        # 每日23:50写新表头（只触发一次）
        if hour == 23 and minute >= 50 and not daily_reset_done:
            print("\n🕦 到达23:50，写入新 Header")
            init_header()
            daily_reset_done = True

        # 新的一天，重置 daily_reset_done
        if hour == 0 and minute < 50:
            daily_reset_done = False

        time.sleep(30)  # 每 30 秒检查一次

if __name__ == "__main__":
    main_loop()
