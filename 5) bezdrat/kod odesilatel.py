import network
import socket
from machine import Pin
import time

network.country('CZ')
tlacitko = Pin(16, Pin.IN, Pin.PULL_UP)

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.ifconfig(('192.168.4.2', '255.255.255.0', '192.168.4.1', '8.8.8.8'))

# Připojujeme se jen pomocí názvu sítě, bez hesla
sta.connect('PicoSit')

print("Hledám otevřenou síť PicoSit...")

max_pokusu = 15
while max_pokusu > 0:
    if sta.isconnected():
        break
    max_pokusu -= 1
    print("Čekám... chybový kód stavu:", sta.status())
    time.sleep(1)

if sta.isconnected():
    print("Úspěšně připojeno! Moje IP:", sta.ifconfig()[0])
else:
    print("Furt nic. Zkontroluj, jestli Pico 2 opravdu vysílá.")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
adresa_prijimace = ('192.168.4.1', 5000)

minuly_stav = 1

while True:
    aktualni_stav = tlacitko.value()
    if aktualni_stav != minuly_stav:
        if aktualni_stav == 0:
            s.sendto("ZAPNI".encode('utf-8'), adresa_prijimace)
            print("Odesláno: ZAPNI")
        else:
            s.sendto("VYPNI".encode('utf-8'), adresa_prijimace)
            print("Odesláno: VYPNI")
        minuly_stav = aktualni_stav
    time.sleep(0.05)