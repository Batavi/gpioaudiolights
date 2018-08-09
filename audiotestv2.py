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

    while(frames > 0):
        currentshard = 0
        for i in range(1,442):
            x = audio.readframes(1)
            val = int.from_bytes(x, byteorder='big')
            currentshard += val
        currentshard = int(currentshard/441)-30000
        lightmap.append(currentshard)
        #if currentshard > 3800:
        #    print(currentshard)
            #GPIO.output(18,GPIO.HIGH)
        #else:
            #GPIO.output(18,GPIO.LOW)
        frames = frames-441
        #print(frames)
        #print(currentshard)
        #time.sleep(0.02)
    print('Frames:')
    print(frames)
    print('Framerate:')
    print(framerate)

    for i in range(1,len(lightmap)):
        print(lightmap[i])

def sound():
    playsound('testaudio.wav')

def lights():
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #GPIO.setup(18,GPIO.OUT)
    for i in range(1,len(lightmap)):
        if lightmap[i] > 3800:
            print(lightmap[i])
            #GPIO.output(18,GPIO.HIGH)
        else:
            print(' ')
            #GPIO.output(18,GPIO.LOW)
        time.sleep(0.02)

precalclights()
#sound()

t1 = Thread(target=lights)
t2 = Thread(target=sound)

t1.start()
t2.start()

#details
#22050
#22000000
