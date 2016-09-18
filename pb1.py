import RPi.GPIO as GPIO   
import time               


class Buzzer(object):
 def __init__(self):
  GPIO.setmode(GPIO.BCM)  
  self.buzzer_pin = 18
  GPIO.setup(self.buzzer_pin, GPIO.IN)
  GPIO.setup(self.buzzer_pin, GPIO.OUT)


 def __del__(self):
  class_name = self.__class__.__name__

## Create the function 'buzz'

 def buzz(self,pitch, duration):   
 
  if(pitch==0):
   time.sleep(duration)
   return
  period = 1.0 / pitch     
  delay = period / 2     
  cycles = int(duration * pitch)  

## Set cycles for GPIO.output

  for i in range(cycles):    
   GPIO.output(self.buzzer_pin, True)   
   time.sleep(delay)   
   GPIO.output(self.buzzer_pin, False)    
   time.sleep(delay)    

 def play(self, tune):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(self.buzzer_pin, GPIO.OUT)
  x=0

## Set the pitch and duration.

  if(tune==1):
    pitches=[number]
    duration=0.1
    for p in pitches:
      self.buzz(p, duration)  
      time.sleep(duration *0.5)


  GPIO.setup(self.buzzer_pin, GPIO.IN)

## Play start

if __name__ == "__main__":
  buzzer = Buzzer()
  buzzer.play(int(1))
GPIO.cleanup()
