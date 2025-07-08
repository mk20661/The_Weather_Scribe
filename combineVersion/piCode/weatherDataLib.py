import threading
import subprocess
import json
import time
from datetime import datetime
import board
import busio
import adafruit_sgp30
import paho.mqtt.client as mqtt
import mqttConfig as mqtt_config



class WeatherGCodeWriter:
    def __init__(self):
        self.canvas_width_mm = 210
        self.canvas_height_mm = 200

        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sgp30 = None
        self.latest_eco2 = -1.0
        self.latest_tvoc = -1.0

        try:
            self.sgp30 = adafruit_sgp30.Adafruit_SGP30(self.i2c)

            self._start_air_quality_thread()
        except Exception as e:
            print("Failed to initialize SGP30 sensor:", e)

    def _start_air_quality_thread(self):
        def update_loop():
            while True:
                try:
                    if self.sgp30:
                        self.latest_eco2 = float(self.sgp30.eCO2)
                        self.latest_tvoc = float(self.sgp30.TVOC)
                        print(f"[SGP30] eCO2={self.latest_eco2}, TVOC={self.latest_tvoc}")
                except Exception as e:
                    print("SGP30 read error:", e)
                time.sleep(1)

        thread = threading.Thread(target=update_loop, daemon=True)
        thread.start()

    def get_air_quality(self):
        return {
            "eco2": self.latest_eco2,
            "tvoc": self.latest_tvoc
        }

    def write_weather_data_to_svg(self, data_entries, svg_file_prefix="weather_data", start_y=320, line_spacing=60):
        font_size = 15

        for i, entry in enumerate(data_entries):
            y = start_y + i * line_spacing
            text_line = "{:<6} {:>12} {:>18} {:>18} {:>8} {:>10} {:>10}".format(
                entry['time'],
                f"{entry['temp']:.1f}",
                f"{entry['humidity']}",
                f"{entry['wind_high']:.1f}",
                f"{entry['rain']:.1f}",
                f"{entry['eco2']:.0f}",
                f"{entry['tvoc']:.0f}"
            )
            temp_svg = f"{svg_file_prefix}_line_{i}.svg"
            cmd = (
                f'vpype text -f futural -s {font_size} "{text_line}" '
                f'translate 10 {y} '
                f'pagesize {self.canvas_width_mm}x{self.canvas_height_mm}mm write ../svgInput/{temp_svg}'
            )
            subprocess.run(cmd, shell=True, check=True)
            return temp_svg

    def svg_to_gcode(self, svg_file="output.svg", gcode_file="output.gcode"):
        cargo_cmd = (
            f"cargo run --manifest-path ../svg2gcode/Cargo.toml -- ../svgInput/{svg_file} "
            f"--off M3 "
            f"--on M5 "
            f"--feedrate 2000 "
            f"--begin 'M3 S90\\nG92 X0 Y0 Z0' "
            f"--end 'G0 X0 Y0 Z0' "
            f"-o ../gcodeOut/{gcode_file}"
        )
        print("[cargo]", cargo_cmd)
        subprocess.run(cargo_cmd, shell=True, check=True)
        print(f"G-code saved to {gcode_file}")

    def write_header_to_svg(self,svg_file="daily_header_a4.svg"):
        lines = [
        f"DAILY CLIMATOLOGICAL SUMMARY for {datetime.date.today().strftime('%b %d, %Y')}".center(100)
        ]

        font_size = 25
        line_spacing = 50
        canvas_width_mm = self.canvas_width_mm
        canvas_height_mm = self.canvas_height_mm
        start_y = 50

        svg_parts = []

        for i, line in enumerate(lines):
            y = start_y + i * line_spacing
            temp_svg = f"header_line_{i}.svg"
            cmd = f"""vpype text -f futural -s {font_size} -a center "{line}" translate 50 {y} pagesize {canvas_width_mm}x{canvas_height_mm}mm write {temp_svg}"""
            print("[vpype]", cmd)
            subprocess.run(cmd, shell=True, check=True)
            svg_parts.append(temp_svg)

        header_text = 'TIME I TEMPERATURES(C) I HUMIDITY (percent) I  WIND (km/h) I UV I RAIN (mm) I PRESSURE(mbar)'
        temp_svg = "header_line_2.svg"
        cmd = (
            f'vpype text -f futural -s 15 "{header_text}" '
            f'translate 20 250 '
            f'pagesize {canvas_width_mm}x{canvas_height_mm}mm '
            f'write ../svgInput/{temp_svg}'
        )
        print("[vpype]", cmd)
        subprocess.run(cmd, shell=True, check=True)
        svg_parts.append(temp_svg)

        x1, y1 = 20, 260
        x2, y2 = 800, 260
        temp_svg = "line.svg"
        cmd = (
            f'vpype line {x1} {y1} {x2} {y2} '
            f'pagesize {canvas_width_mm}x{canvas_height_mm}mm write {temp_svg}'
        )
        print("[vpype]", cmd)
        subprocess.run(cmd, shell=True, check=True)
        svg_parts.append(temp_svg)

        gcode_file = "daily_report_header.gcode"
        self.svg_to_gcode(svg_file, gcode_file)

    def on_connect(self,client, userdata, flags, rc):
        if rc == 0:
            print("MQTT Connected")
            client.subscribe(mqtt_config.TOPIC)
        else:
            print("MQTT Connect failed with code", rc)

    def on_message(self,client, userdata, msg):
        print("Message received!")
        try:
            payload = msg.payload.decode()
            print("[Payload]", payload)

            data = json.loads(payload)

            dt = datetime.fromtimestamp(float(data.get("dateTime", 0)))
            entry = {
                "time": f"{dt.strftime('%H:00')}",
                "temp": float(data["outTemp_C"]),
                "humidity": float(data["outHumidity"]),
                "wind_high": float(data["windGust_kph"]),
                "uv": float(data["UV"]),
                "rain": float(data["dayRain_cm"]),
                "pressure": float(data["pressure_mbar"]),
            }


            self.write_weather_data_to_svg([entry])

            svg_file = "weather_data_line_0.svg"
            self.svg_to_gcode(svg_file, f"{svg_file}.gcode")

        except Exception as e:
            print("Failed to process message:", e)
        finally:
            client.disconnect()