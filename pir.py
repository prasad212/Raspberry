from gpiozero import Button,Buzzer,MotionSensor
from time import sleep
but=Button(2)
bz=Buzzer(3)
pir=MotionSensor(26)
while True:
    pir.wait_for_motion()
    print('Motion is Detected',pir.motion_detected)
    bz.on()
    sleep(0.5)
    bz.off()
