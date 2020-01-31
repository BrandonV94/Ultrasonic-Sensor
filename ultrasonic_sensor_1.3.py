import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TRIG = 7    # GPIO pin 7
TRIG1 = 5   # GPIO pin 5

ECHO = 12   # GPIO pin 12
ECHO1 = 16  # GPIO pin 16

LED = 11    # LED pin 11
LED1 = 15   # LED pin 15

#Global Variables 
inch = 0
cm = 0
inch1 = 0
cm1 = 0

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(TRIG1,GPIO.OUT)

GPIO.output(TRIG,0)     #Set TRIG low
GPIO.output(TRIG1,0)    #Set TRIG1 low

GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(ECHO1,GPIO.IN)

#LED Test
def ledTest() :
    GPIO.output(LED,1)      
    GPIO.output(LED1,1)     
    GPIO.output(LED,0)      
    GPIO.output(LED1,0)     
    return

#Activate Sensor
def sensorValue(x, y, c, i) : #x = trig, y= echo, c = cm, and i = inches
    global cm
    global cm1
    global inch
    global inch1
    GPIO.output(x,1)
    time.sleep(0.00001)     # Wait 10microseconds
    GPIO.output(x,0)

    while GPIO.input(y) == 0:    # While loop will continue until input is high
        pass                        # pass in a while loop means do nothing
    start = time.time()

    while GPIO.input(y) == 1:    # While loop will continue until input is low
        pass
    stop = time.time()
    
    c = (stop - start) * 170 * 100  #Multiply by 100 because time is in ms
    cm = c
    cm1 = c

    i = c * 0.393701                #Multipy cm by 0.3937 because 1cm is equal to 0.393701
    inch = i
    inch1 = i
    return

#Print Value
def printValue(c, i, l):
    if (i < 10):
        GPIO.output(l,1)
        time.sleep(5)
    else:
        GPIO.output(l,0)
        time.sleep(5)
        
    print "%.2f cm" %c
    print "%.2f inch" %i
    return

#Main
time.sleep(0.1)     # Wait 100ms
ledTest()
print "Starting Measurement..."

try:
    while True:
        #Sensor 1
        sensorValue(TRIG, ECHO, cm, inch)
        printValue(cm, inch, LED)
        
        time.sleep(.001)

        #Sensor 2
        sensorValue(TRIG1, ECHO1, cm1, inch1)
        printValue(cm1, inch1, LED1)
        print "--------------"
        

except KeyboardInterrupt:
    GPIO.cleanup()
