# Raspberry Pi Robot

We are going to move from Arduino to Raspberry Pi. The reasons to move
from Arduino to Raspberry Pi would be generally:

* Greater ease of communication through wifi and networking
* Need for greater computational power

One challenge of working with Raspberry Pi is that it doesn't come 
with voltage regulation, and is fairly sensitive to the fluctuations
in power. Therefore we need to create good steady 5V of voltage draw
for our pis to work from. This is no problem when our pis are plugged 
in, but when we are working on battery we will need to have voltage 
regulation circuit. 

## Voltage Regulation Circuit

It looks like we don't have enough power cords right now, so some 
will have partner up, or simply work with power cords for the moment.

### Directions for the Voltage Regulator

The voltage regulator itself has three pins. Those pins with 
black facing are:

* Adjust(1), Vout(2), Vin(3)

We will set up 2 different power rails. One for the unregulated (high)
power and the other for the regulated (low) power.

* First plug the voltage regulator with the black facing the low voltage
rail. 
* Next, connect capicitors from each voltage pin of the regulator 
to ground rail on the high voltage side.
* Next, a 1K ohm Resistor connects Vout of the regulator to 
the adjust pin of the regulator.
* Place a wire from V_out to low voltage power rail. 
* Place a wire from the ground of the low voltage rail to the 
ground of the high voltage rail.
* Place a wire from the high voltage rail ground to the adjust pin 
of the regulator.
* Finally use a wire to connect high voltage power rail to Vin

and heat sink.

Now connect Raspberry Pi to Computer

First step is already done:
Jerry's process:

https://notes.jerrywang.website/robotics/CS570/day8.html

Jerry has flashed the raspbian operating system (in our google drive). 

Renamed the device so that it would be unique on our network. 

Now we should ssh into the device. 

Connect to Robotic-5 wifi, then the password is choate7407


mkdir Robot

git init

nano motor1.py

b3d2bb9cf8263c0c17cfacc708dd8eb84e2d16bc