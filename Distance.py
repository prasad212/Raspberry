from gpiozero import DistanceSensor,Buzzer
from time import sleep

sn = DistanceSensor(echo=24,trigger=18)
bz = Buzzer(3)

while True:
    if sn.distance <10:
        print('distance is less than 10',sn.distance)
        bz.on()
        sleep(1)
        bz.off()
    else:
      print ('Distance :',dist)
    sleep (1)
