//  Sett opp radioen med ønsket gruppe (begge micro:bit-ene må ha samme gruppe)
radio.setGroup(1)
//  Globale variabler som holder styr på om senderne for hver knapp er aktiv
let A_active = false
let B_active = false
//  Funksjon for knapp A: toggle sending med melding "A: Sender på" / "A: Sender av"
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    A_active = !A_active
    //  Bytt tilstand
    if (A_active) {
        radio.sendString("A: Sender på")
        basic.showIcon(IconNames.Yes)
    } else {
        radio.sendString("A: Sender av")
        basic.showIcon(IconNames.No)
    }
    
})
//  Funksjon for knapp B: toggle sending med EN ANNEN melding "B: Starter sending" / "B: Stopper sending"
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    B_active = !B_active
    //  Bytt tilstand
    if (B_active) {
        radio.sendString("B: Starter sending med annen melding")
        basic.showIcon(IconNames.Heart)
    } else {
        radio.sendString("B: Stopper sending med annen melding")
        basic.showIcon(IconNames.Snake)
    }
    
})
//  Funksjon som blir kalt ved mottak av melding via radio
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
//  Hovedløkke som sender "live"-meldinger så lenge en av knappene er aktive.
while (true) {
    if (A_active) {
        radio.sendString("A: Live melding")
    }
    
    if (B_active) {
        radio.sendString("B: Live melding")
    }
    
    basic.pause(1000)
}
