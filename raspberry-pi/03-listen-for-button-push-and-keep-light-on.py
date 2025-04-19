import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

in_pin = 18
out_pin = 12

gpio.setup(out_pin, gpio.OUT)

gpio.setup(in_pin, gpio.IN, pull_up_down=gpio.PUD_UP)

led_state = 0
button_state = 1
button_state_old = 1
try:
    while True:
        button_state = gpio.input(in_pin)
        if button_state == 1 and button_state_old == 0:
            led_state = not led_state
            gpio.output(out_pin, led_state)
            print(led_state, end = ' ')
        button_state_old = button_state
        sleep(.01)
except KeyboardInterrupt:
    print('\ncleaning up; exiting')
    gpio.cleanup()
