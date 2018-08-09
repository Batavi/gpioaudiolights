import wave
import time
#import RPi.GPIO as GPIO
from playsound import playsound
from threading import Thread

lightmap = [0]

def precalclights():
    audio = wave.open('testaudio.wav', 'rb')
    frames = audio.getnframes()
    framerate = audio.getframerate()
    roundframes = 10*int(frames/10)
    framesin02s = 4410
    shard = 0
    chunks = int(roundframes/framesin02s)
    print(roundframes)
    print(chunks)
    for i in range(1,chunks):
        shard = 0
        for y in range(1,4411):
            x = audio.readframes(1)
            val = int.from_bytes(x, byteorder='big')
            shard += val
        lightmap.append(int(shard/4410)-30000)

        #lightmap.append()
        #if currentshard > 3800:
        #    print(currentshard)
            #GPIO.output(18,GPIO.HIGH)
        #else:
            #GPIO.output(18,GPIO.LOW)

    #for i in range(1,len(lightmap)):
    #    print(lightmap[i])

def sound():
    playsound('testaudio.wav')

def lights():
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #GPIO.setup(18,GPIO.OUT)
    for i in range(1,len(lightmap)):
        if lightmap[i] > 3100:
            print(lightmap[i])
            #GPIO.output(18,GPIO.HIGH)
        else:
            print(' ')
            #GPIO.output(18,GPIO.LOW)
        time.sleep(0.2)

precalclights()
#sound()

t1 = Thread(target=lights)
t2 = Thread(target=sound)

t1.start()
time.sleep (3)
t2.start()

#details
#22050
#22000000
