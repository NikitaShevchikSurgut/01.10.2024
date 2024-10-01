import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

led = [2, 3, 4, 17, 27, 22, 10, 9]

comp = 14

troyka = 13

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(led, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT)

GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, 1)

def decimal2binary(value):            #перевод десятичного числа в двоичное
    return [int(element) for element in bin(value)[2:].zfill(8)]

t = 0.0

def adc(T):                     #измерение напряжения  
    current = 128
    for i in range(0, 8):
        GPIO.output(dac, decimal2binary(int(current)))
        time.sleep(0.01)
        T +=0.01
        if (GPIO.input(comp) == 0):
            current += 128/2**(i+1)
        else:
            current -= 128/2**(i+1)
            
    output_current = 3.3/256*current
    return output_current, T, current

try:
    while(1):
        print('напряжение на входе S: ', adc(t)[0],' В,   затрачено времени: ', adc(t)[1], ' с')
        #print(decimal2binary(int(adc(t)[2])))
        value = int(adc(t)[2])
        if (value < 32):
            value = 0
        if (value >= 32 and value < 64):
            value = 1
        if (value >= 64 and value < 96):
            value = 3
        if (value >= 96 and value < 128):
            value = 7
        if (value >= 128 and value < 160):
            value = 15
        if (value >= 160 and value < 192):
            value = 31
        if (value >= 192 and value < 224):
            value = 63
        if (value >= 224 and value < 255):
            value = 127
        if (value == 255):
            value = 255
        print(value)
       
        
        GPIO.output(led, decimal2binary(value))
    

finally:
    GPIO.output(dac, decimal2binary(0))
