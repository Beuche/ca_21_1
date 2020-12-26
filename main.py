led_an=False
while True:
    if input.button_is_pressed(Button.A):
        if led_an==True:
            basic.set_led_color(0x005000)
            led_an=False
        else:
            basic.set_led_color(0x000000)
            led_an=True
    while input.button_is_pressed(Button.A):
        pass
