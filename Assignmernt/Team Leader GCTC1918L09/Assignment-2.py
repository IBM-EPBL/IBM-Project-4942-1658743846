import random
from time import*
ideal=True
while(ideal):
    Temp=random.randint(0,100)
    Humi=random.randint(10,50)
    if Temp>40 and Humi<30:
        print("Temperature=",Temp,"Humidity=",Humi)
        print("         Alarm ON         ")
        ideal=False
    else:
        print("Temperature=",Temp,"Humidity",Humi)
        sleep(1);
