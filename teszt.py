import time
import pyautogui
import pygetwindow as gw
import subprocess
import ctypes
import keyboard 

packet_tracer_path = r"C:\Program Files\Cisco Packet Tracer 8.2.2\bin\PacketTracer.exe"
subprocess.Popen(packet_tracer_path)
time.sleep(15)
pyautogui.press('down')
