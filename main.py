led_an=False
while True:
    if input.button_is_pressed(Button.A):
        if led_an==True:
            basic.set_led_color(0x00500)
        else:
