import threading
import subprocess
import json
import time
import datetime
import board
import busio
import adafruit_sgp30
import paho.mqtt.client as mqtt
import mqttConfig as mqtt_config
import serial
from adafruit_pm25.uart import PM25_UART


class WeatherGCodeWriter:
    def __init__(self):
        self.canvas_width_mm = 245
        self.canvas_height_mm = 230

        self.base_hour = None 
        self.last_header_date = None

        #update eco2
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sgp30 = None
        self.latest_eco2 = -1.0

        #update PM2.5
        self.pm25 = None
        self.latest_pm25 = -1.0

        # Initialize sgp30 sensor
        try:
            self.sgp30 = adafruit_sgp30.Adafruit_SGP30(self.i2c)
            print("SGP30 serial:", [hex(i) for i in self.sgp30.serial])

            print("Warming up sensor for 15 seconds...")
            for _ in range(15):
                time.sleep(1)
                print(".", end="", flush=True)
            print("\nSensor ready.")

        except Exception as e:
            print("Failed to initialize SGP30 sensor:", e)

        # Initialize PM2.5 sensor
        try:
            pm5003_reset_pin = None
            pm5003_uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.25)
            self.pm25 = PM25_UART(pm5003_uart, pm5003_reset_pin)
            print("PM2.5 sensor initialized.")
        except Exception as e:
            print("Failed to initialize PM2.5 sensor:", e)

        # Start background thread
        self._start_air_quality_thread()

    def _start_air_quality_thread(self):
        def update_loop():
            while True:
                try:
                    if self.sgp30:
                        self.latest_eco2 = float(self.sgp30.eCO2)
                        print(f"[SGP30] eCO2={self.latest_eco2} ppm")
                    if self.pm25:
                        pm_data = self.pm25.read()
                        self.latest_pm25 = float(pm_data["pm25 standard"])
                        print(f"[PM2.5] PM2.5={self.latest_pm25} µg/m³")
                except Exception as e:
                    print("sensor read error:", e)
                time.sleep(1)

        thread = threading.Thread(target=update_loop, daemon=True)
        thread.start()

    def get_air_quality(self):
        return {
            "eco2": self.latest_eco2,
            "pm25": self.latest_pm25
        }

    def write_weather_data_to_svg(self, data_entries, svg_file_prefix="weather_data_time_", start_y=20, line_spacing=35):
        font_size = 24
        now = datetime.datetime.now()

        if self.last_header_date != datetime.date.today():
            self.base_hour = now.hour
            self.last_header_date = datetime.date.today()

        relative_hour = now.hour - self.base_hour
        if relative_hour < 0:
            relative_hour += 24

        y = start_y + relative_hour * line_spacing
        for i, entry in enumerate(data_entries):
            #y = start_y + i * line_spacing
            text_line = "{:<0} {:>12} {:>10} {:>12} {:>7} {:>6} {:>5}".format(
                entry['time'],
                f"{entry['temp']:.1f}",
                f"{entry['humidity']}",
                f"{entry['wind_high']:.1f}",
                f"{entry['rain']:.1f}",
                f"{entry['eco2']:.0f}",
                f"{entry['pm25']:.0f}"
            )
        temp_svg = f"../svgInput/{svg_file_prefix}{datetime.datetime.now().hour}.svg"
        cmd = (
            f'vpype text -f futural -s {font_size} "{text_line}" '
            f'translate 5 {y} '
            f'pagesize {self.canvas_width_mm}x{self.canvas_height_mm}mm write ../svgInput/{temp_svg}'
        )

        with open("vpype_log.txt", "a") as log_file:
            log_file.write(f"[{datetime.datetime.now()}] {cmd}\n")
        subprocess.run(cmd, shell=True, check=True)

    def svg_to_gcode(self, svg_file="output.svg", gcode_file="output.gcode"):
        cargo_cmd = (
            f"cargo run --manifest-path ../svg2gcode/Cargo.toml -- ../svgInput/{svg_file} "
            f"--off M3 "
            f"--on M5 "
            f"--feedrate 3000 "
            f"--begin 'M3 S90\nG92 X0 Y0 Z0' "
            f"--end 'G0 X0 Y0 Z0' "
            f"-o ../gcodeOut/{gcode_file}"
        )
        print("[cargo]", cargo_cmd)
        subprocess.run(cargo_cmd, shell=True, check=True)
        print(f"G-code saved to {gcode_file}")

    def write_header_to_svg(self,svg_file="../svgInput/daily_header.svg"):
        self.base_hour = 0
        self.last_header_date = datetime.date.today()
        lines = [
        "DAILY WEATHER LOG".center(48),
        f"{datetime.date.today().strftime('%B')} {datetime.date.today().day} {datetime.date.today().year}".center(40),
        "UCL East".center(36)
    ]

        font_size = 50
        line_spacing = 50
        canvas_width_mm = self.canvas_width_mm
        canvas_height_mm = self.canvas_height_mm
        start_y = 30

        svg_parts = []

        for i, line in enumerate(lines):
            y = start_y + i * line_spacing
            temp_svg = f"../svgInput/header_line_{i}.svg"
            cmd = f"""vpype text -f futural -s {font_size} -a center "{line}" translate 30 {y} pagesize {canvas_width_mm}x{canvas_height_mm}mm write {temp_svg}"""
            print("[vpype]", cmd)
            subprocess.run(cmd, shell=True, check=True)
            svg_parts.append(temp_svg)

        header_text = 'TIME I TEMPERATURES I HUMIDITY I  WIND  I RAIN I ECO2 I PM2.5'
        temp_svg = "../svgInput/header_line_3.svg"
        cmd = (
            f'vpype text -f futural -s 26 "{header_text}" '
            f'translate 0 170 '
            f'pagesize {canvas_width_mm}x{canvas_height_mm}mm '
            f'write {temp_svg}'
        )
        print("[vpype]", cmd)
        subprocess.run(cmd, shell=True, check=True)
        svg_parts.append(temp_svg)

        header_text_unit = '     I       C         I percent  I  KM/H I MM   I PPM  I ug/m³'
        temp_svg = "../svgInput/header_unit.svg"
        cmd = (
            f'vpype text -f futural -s 26 "{header_text_unit}" '
            f'translate 0 200 '
            f'pagesize {canvas_width_mm}x{canvas_height_mm}mm '
            f'write {temp_svg}'
        )
        print("[vpype]", cmd)
        subprocess.run(cmd, shell=True, check=True)
        svg_parts.append(temp_svg)
        
        x1, y1 = 20, 220
        x2, y2 = 810, 220
        temp_svg = "../svgInput/line.svg"
        cmd = (
            f'vpype line {x1} {y1} {x2} {y2} '
            f'pagesize {canvas_width_mm}x{canvas_height_mm}mm write {temp_svg}'
        )
        print("[vpype]", cmd)
        subprocess.run(cmd, shell=True, check=True)
        svg_parts.append(temp_svg)

        merge_cmd = ["vpype"]
        for svg in svg_parts:
            merge_cmd += ["read", svg]
        merge_cmd += ["write", svg_file]
        print("[merge]", " ".join(merge_cmd))
        subprocess.run(merge_cmd, check=True)

        print(f"SVG written to: {svg_file}")

        gcode_file = "../gcodeOut/daily_report_header.gcode"
        self.svg_to_gcode(svg_file, gcode_file)

def send_gcode_to_arduino(gcode_file, port='/dev/tty.usbmodem1201', baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate, timeout=2)
        time.sleep(2)

        ser.reset_input_buffer()

        with open(gcode_file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            print(f">>> Sending: {line}")
            ser.write((line + '\n').encode())

            while True:
                response = ser.readline().decode().strip()
                if response:
                    print(f"<<< Received: {response}")
                if "ok" in response.lower():
                    break

        print("All G-code lines sent successfully.")
        
    except serial.SerialException as e:
        print("Serial error:", e)
    except FileNotFoundError:
        print(f"File not found: {gcode_file}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial connection closed.")

def paperRoll(stepSize=20, port="/dev/tty.usbmodem1201", baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate, timeout=2)
        time.sleep(2)
        ser.reset_input_buffer()

        commands = [
            f"G0 Z{stepSize} F3000",
            "G92 Z0 F3000"
        ]

        for cmd in commands:
            print(f">>> Sending: {cmd}")
            ser.write((cmd + "\n").encode())

            while True:
                response = ser.readline().decode().strip()
                if response:
                    print(f"<<< Received: {response}")
                if "ok" in response.lower():
                    break

        print("paperRoll complete")

    except serial.SerialException as e:
        print("Serial error:", e)
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial connection closed.")