let led_an = false
while (true) {
    if (input.buttonIsPressed(Button.A)) {
        if (led_an == true) {
            basic.setLedColor(0x005000)
            led_an = false
        } else {
            basic.setLedColor(0x000000)
            led_an = true
        }
        
    }
    
    while (!input.buttonIsPressed(Button.A)) {
        
    }
}
