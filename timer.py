import os
import time


s=0
m=0

while s<=60:
    os.system('cls')
    print (m, 'Minutes', s, 'Seconds')
    time.sleep(1)
    s+=1
    if s==60:
        m+=1
        s=0

#taken from http://stackoverflow.com/questions/15802554/how-to-make-a-timer-program-in-python
