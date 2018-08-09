import wave
import time
#import RPi.GPIO as GPIO
from playsound import playsound
from threading import Thread

def lights():
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #GPIO.setup(18,GPIO.OUT)
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
        if currentshard > 3800:
            print(currentshard)
            #GPIO.output(18,GPIO.HIGH)
        #else:
            #GPIO.output(18,GPIO.LOW)
        frames = frames-441
        #print(frames)
        #print(currentshard)
        time.sleep(0.01)
    print('Frames:')
    print(frames)
    print('Framerate:')
    print(framerate)

def sound():
    playsound('testaudio.wav')

#lights()
#sound()

t1 = Thread(target=lights)
t2 = Thread(target=sound)

t1.start()
t2.start()

#details
#22050
#22000000
