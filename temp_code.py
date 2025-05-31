# telemetry_server.py
import socket
import json
import subprocess
import os
import sys

HOST = '127.0.0.1'
PORT = 5050

def start_trackmania():
    # Adjust the path to the Trackmania executable as necessary
    trackmania_path = "D:\SteamLibrary\steamapps\common\Trackmania\Trackmania"  # Example path
    try:
        subprocess.Popen(trackmania_path)
        print("🟢 Trackmania started successfully.")
    except Exception as e:
        print(f"⚠️ Failed to start Trackmania: {e}")

def start_server():
    print(f"🟢 Starting server on {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        print(f"✅ Connection from {addr}")

        with conn:
            buffer = ""
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                buffer += data
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    try:
                        telemetry = json.loads(line)
                        print(telemetry)  # Process or store the data here
                    except json.JSONDecodeError as e:
                        print(f"⚠️ Failed to parse: {line} | {e}")

if __name__ == "__main__":
    start_trackmania()  # Start Trackmania before starting the server
    start_server()
