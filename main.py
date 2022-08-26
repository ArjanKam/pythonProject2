from machine import Pin

PIN_D2: int = 2

led = Pin(PIN_D2, Pin.OUT)

while True:

    led.on()
