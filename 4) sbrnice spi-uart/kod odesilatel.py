from machine import UART, Pin
import time

# UART na pinech GP0 (TX) a GP1 (RX)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Tlačítko na pinu GP16 s vnitřním pull-up rezistorem
tlacitko = Pin(16, Pin.IN, Pin.PULL_UP)

# Uložení výchozího stavu (1 = uvolněno, 0 = stisknuto)
minuly_stav = 1

while True:
    aktualni_stav = tlacitko.value()
    
    # Pokud se stav změnil (došlo ke stisku nebo uvolnění)
    if aktualni_stav != minuly_stav:
        if aktualni_stav == 0:
            uart.write("ZAPNI\n".encode('utf-8'))
            print("Odesláno: ZAPNI")
        else:
            uart.write("VYPNI\n".encode('utf-8'))
            print("Odesláno: VYPNI")
            
        # Aktualizace stavu, abychom povel neodesílali znovu dokola
        minuly_stav = aktualni_stav
        
    # Krátká pauza pro eliminaci mechanických zákmitů tlačítka (debouncing)
    time.sleep(0.05)