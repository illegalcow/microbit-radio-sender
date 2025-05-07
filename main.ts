//  Sett opp radioen: gruppen er identisk for sender og mottaker
radio.setGroup(1)
radio.setTransmitPower(7)
//  Valgfritt: juster overføringsstyrken
//  Funksjon som sendes når knapp A trykkes
//  Viser et ikon
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("Hei fra sender!")
    //  Sender en melding med radio
    basic.showIcon(IconNames.Happy)
})
//  Funksjon som kalles når en melding mottas via radio
//  Viser den mottatte meldingen
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
