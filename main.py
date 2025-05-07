# Sett opp radioen: gruppen er identisk for sender og mottaker
radio.set_group(1)
radio.set_transmit_power(7)  # Valgfritt: juster overføringsstyrken

# Funksjon som sendes når knapp A trykkes
def on_button_pressed_a():
    radio.send_string("Hei fra sender!")  # Sender en melding med radio
    basic.show_icon(IconNames.HAPPY)        # Viser et ikon
input.on_button_pressed(Button.A, on_button_pressed_a)

# Funksjon som kalles når en melding mottas via radio
def on_received_string(receivedString: str):
    basic.show_string(receivedString)  # Viser den mottatte meldingen
radio.on_received_string(on_received_string)
