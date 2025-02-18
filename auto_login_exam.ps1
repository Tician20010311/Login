# Beállítások
$packetTracerPath = "C:\Program Files\Cisco Packet Tracer 8.2.2\bin\PacketTracer.exe" # Módosítsd a pontos elérési úttal
$email = "packettracer@vasvari.hu"
$password = "VPpt2024."


# UI Automation betöltése
Add-Type -AssemblyName System.Windows.Forms

function Disable-CapsLock {
    $wsh = New-Object -ComObject WScript.Shell
    if ([System.Windows.Forms.Control]::IsKeyLocked("CapsLock")) {
        Write-Output "Caps Lock be van kapcsolva, kikapcsolás..."
        $wsh.SendKeys("{CAPSLOCK}")
        Start-Sleep -Milliseconds 500
    } else {
        Write-Output "Caps Lock már ki van kapcsolva."
    }
}

# Futtassuk a Caps Lock kikapcsoló funkciót
Disable-CapsLock

# Packet Tracer indítása
Start-Process -FilePath $packetTracerPath
Start-Sleep -Seconds 5  # Várunk, hogy a program elinduljon

# Packet Tracer ablak előtérbe hozása
$packetTracer = Get-Process | Where-Object { $_.ProcessName -like "PacketTracer*" } | Select-Object -First 1
if ($packetTracer) {
    [UserInput]::SetForegroundWindow($packetTracer.MainWindowHandle)
    Start-Sleep -Seconds 2  # Kis várakozás
    [UserInput]::ShowWindow([System.IntPtr]$packetTracer.MainWindowHandle, 5) # SW_SHOW
    [UserInput]::SetForegroundWindow([System.IntPtr]$packetTracer.MainWindowHandle)
}
Start-Sleep -Milliseconds 1000
[System.Windows.Forms.SendKeys]::SendWait("{TAB}") # Bejelentkezés
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}") # Bejelentkezés
Start-Sleep -Milliseconds 7000

# E-mail cím beírása
[System.Windows.Forms.SendKeys]::SendWait("$email")
Start-Sleep -Milliseconds 3000
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}") # Jelszómezőre lépés
Start-Sleep -Milliseconds 3000

# Jelszó beírása
[System.Windows.Forms.SendKeys]::SendWait("$password")
Start-Sleep -Milliseconds 3000
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}") # Bejelentkezés

Write-Output "Bejelentkezési folyamat elindítva!"
