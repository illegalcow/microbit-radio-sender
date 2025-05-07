from microbit import *
import radio

radio.on()  # Slå på radioen

while True:
    if button_a.is_pressed():
        radio.send("Hei fra sender!")  # Send melding ved knappetrykk
        display.show(Image.HAPPY)
        sleep(1000)  # Kort pause før skjermen tømmes
        display.clear()

    message = radio.receive()  # Mottar melding
    if message:
        display.scroll(message)  # Viser mottatt melding
