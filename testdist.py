from gpiozero import DistanceSensor,Buzzer,LED,Button,MotionSensor
from time import sleep

sn = DistanceSensor(echo=24,trigger=18)
bz = Buzzer(3)
bu=Button(2)
pir=MotionSensor(26)
while True:
    
        dist=sn.distance*100
        if dist <25:
            print('distance is less than 20 : ',dist )
            pir.wait_for_motion()
            print('moving object nearby : ',dist )
            bz.on()
            sleep(0.5)
            bz.off()
        else:   
            sleep(0.5)
            print('Distance is :- ',dist)
            
        
