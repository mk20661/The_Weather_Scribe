import serial
import time

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
            f"G0 Z{stepSize}",
            "G92 Z0"
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

        print("✅ paperRoll complete")

    except serial.SerialException as e:
        print("Serial error:", e)
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial connection closed.")

# 使用方法（举例）
send_gcode_to_arduino("daily_report_header_copy.gcode", port="/dev/tty.usbmodem21201")
#paperRoll(stepSize=20, port="/dev/tty.usbmodem21201", baudrate=115200)
