from machine import Pin
import time

# Nastavení výstupu pro EXTERNÍ LED na pinu GP15
led = Pin(15, Pin.OUT)

# Nastavení vstupu pro tlačítko na pinu GP14 s interním pull-down rezistorem
tlacitko = Pin(14, Pin.IN, Pin.PULL_DOWN)

print("Připraveno! Stiskněte tlačítko pro rozsvícení LED.")

while True:
    # Přečte, zda je tlačítko stisknuté (1) nebo ne (0)
    stav_tlacitka = tlacitko.value()
    
    if stav_tlacitka == 1:
        # Pošle napětí na pin 15 -> LED svítí
        led.value(1)
    else:
        # Vypne napětí na pinu 15 -> LED zhasne
        led.value(0)
        
    time.sleep(0.05)