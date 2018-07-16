from gpiozero import Button,Buzzer
from time import sleep
but=Button(2)
bz=Buzzer(3)
while True:
    but.wait_for_press()
    print('Kela',but.is_pressed)
    bz.on()
    sleep(0.5)
    bz.off()
