import os
import time as ti

h = int(input("Enter hour : "))
m = int(input("Enter minute : "))
s = int(input("Enter second : "))

hour = h*3600
minute = m*60

time = str(hour+minute+s)

os.system("shutdown /s /t "+time)

time = int(time)
for i in range(time,0,-1):
    os.system("cls")
    h = str(int(i / 3600))
    m = str(int((i%3600)/60))
    s = str(int((i%3600)%60))
    print(h+" : "+m+" : "+s)
    ti.sleep(1)
