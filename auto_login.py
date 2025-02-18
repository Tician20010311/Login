import time
import pyautogui
import pygetwindow as gw
import subprocess
import ctypes
import keyboard 
import threading


# Beállítások
packet_tracer_path = r"C:\Program Files\Cisco Packet Tracer 8.2.2\bin\PacketTracer.exe"
visual_studio_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe"
ptpassword = "VPpt2024."
vspassword = "VPMs2023"



# Caps Lock állapotának lekérdezése
def get_caps_lock_state():
    # Beolvassa a billentyűzet állapotát
    return ctypes.windll.user32.GetKeyState(0x14) & 0x0001
# Caps Lock kikapcsolása
def toggle_caps_lock():
    ctypes.windll.user32.keybd_event(0x14, 0, 0, 0)  # Caps Lock lenyomása
    ctypes.windll.user32.keybd_event(0x14, 0, 2, 0)  # Caps Lock felengedése
# Ha a Caps Lock be van kapcsolva, kikapcsoljuk
if get_caps_lock_state() == 1:
    toggle_caps_lock()


# Packet Tracer indítása
subprocess.Popen(packet_tracer_path)
time.sleep(15)  # Várunk, hogy a program elinduljon


#Multiuser ablak kezelése
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)

# Packet Tracer ablak előtérbe hozása
packet_tracer_window = None
while packet_tracer_window is None:
    time.sleep(1)
    windows = gw.getWindowsWithTitle("Packet Tracer")
    if windows:
        packet_tracer_window = windows[0]

# Az ablak fókuszálása
packet_tracer_window.activate()
time.sleep(5)

for i in range(0, 3):
    pyautogui.press('tab')  # Bejelentkezési mező
    time.sleep(1)
# Mararadjon bejelentkezve gomb megnyomása
pyautogui.press('enter')  
time.sleep(15)
for i in range(0, 9):
    pyautogui.press('tab') 
    time.sleep(1)
pyautogui.press('enter')  # Bejelentkezés
time.sleep(20)

# E-mail cím beírása (külön kezeljük az @ karaktert)
pyautogui.write('packettracer')
keyboard.write('@')  # A keyboard modul segítségével írjuk be az @ karaktert
pyautogui.write('vasvari.hu')
time.sleep(3)
pyautogui.press('enter')  # Jelszó mezőre lépés
time.sleep(3)
# Jelszó beírása
pyautogui.write(ptpassword)
time.sleep(3)
pyautogui.press('enter')  # Bejelentkezés
time.sleep(10)
packet_tracer_window.activate()
time.sleep(1)  # Kis várakozás az aktiválás után

try:
    # Visual Studio megnyitása
    subprocess.Popen(visual_studio_path)
    time.sleep(10)  # Várakozás, amíg a program elindul
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')

except FileNotFoundError:
    print("Hiba: Nem található a Visual Studio futtatható fájlja. Ellenőrizd az elérési útvonalat!")
except Exception as e:
    print(f"Hiba történt: {e}")