# Sett opp radioen med ønsket gruppe (begge micro:bit-ene må ha samme gruppe)
radio.set_group(1)

# Globale variabler som holder styr på om senderne for hver knapp er aktiv
A_active = False
B_active = False

# Funksjon for knapp A: toggle sending med melding "A: Sender på" / "A: Sender av"
def on_button_pressed_a():
    global A_active
    A_active = not A_active  # Bytt tilstand
    if A_active:
        radio.send_string("A: Sender på")
        basic.show_icon(IconNames.YES)
    else:
        radio.send_string("A: Sender av")
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Funksjon for knapp B: toggle sending med EN ANNEN melding "B: Starter sending" / "B: Stopper sending"
def on_button_pressed_b():
    global B_active
    B_active = not B_active  # Bytt tilstand
    if B_active:
        radio.send_string("B: Starter sending med annen melding")
        basic.show_icon(IconNames.HEART)
    else:
        radio.send_string("B: Stopper sending med annen melding")
        basic.show_icon(IconNames.SNAKE)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Funksjon som blir kalt ved mottak av melding via radio
def on_received_string(receivedString: str):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

# Hovedløkke som sender "live"-meldinger så lenge en av knappene er aktive.
while True:
    if A_active:
        radio.send_string("A: Live melding")
    if B_active:
        radio.send_string("B: Live melding")
    basic.pause(1000)  # Sender et nytt live signal hvert sekund
