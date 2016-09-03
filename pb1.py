## {LICENSE}

## Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
## Upstream-Name: buano
## Source: https://github.com/cosmosproject15/pi

## Files: bp1.py, README, buano
## Copyright: 2016 C O S M O S Project. <cosmosp2016@gmail.com>

## License: GPL-2.0+

## Files: pi/buano/README
## Copyright: 2016 C O S M O S Project. <cosmosp2016@gmail.com>
## License: GPL-2.0+

##  License: GPL-2.0+
##  This package is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##  .
##  This package is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##  .
##  You should have received a copy of the GNU General Public License
##  along with this program. If not, see <https://www.gnu.org/licenses/>
##  .
##  On Debian systems, the complete text of the GNU General
##  Public License version 2 can be found in "/usr/share/common-licenses/GPL-2".

## # Please also look if there are files or directories which have a
## # different copyright/license attached and list them here.
## # Please avoid picking licenses with terms that are more restrictive than the
## # packaged work, as it may make Debian's contributions unacceptable upstream.



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
