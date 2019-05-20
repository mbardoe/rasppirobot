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

![voltage regulator breadboard](https://github.com/mbardoe/rasppirobot/blob/master/assets/VoltageRegulator_bb.png)


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

The voltage regulator converts excess voltage to heat. You may
want to add one of the heat sinks that are in the raspberry pi box 
to the voltage regulator to help make sure the voltage regulator 
doesn't fail and then fry your Raspberry Pi.


## Connect Raspberry Pi to Computer

Much of this work has been done for us by Jerry. Raspberry Pi's need
to have an operating system installed. Then they need to be given 
credentials to the wifi, and in our case, they need to be renamed so
that we can create communication between them. They need to have 
certain communication protocols allowed in their settings. All of this
has been done by Jerry, and you can see his logging of the process at
https://notes.jerrywang.website/robotics/CS570/day8.html . There 
is also a script that automates this process. That script is unnecessary
unless you want to do this process with multiple pis at once. Importantly:

* Jerry has flashed the raspbian operating system ( a copy you can find in our google drive). 
* Renamed the device so that it would be unique on our network. 

### Connecting via wifi to your pi

Plug in your raspberry pi. Then open terminal (or equivalent) on your computer.
We will then use a protocal called ```ssh``` to connect directly to the pi.
```ssh``` is called [Secure shell](https://en.wikipedia.org/wiki/Secure_Shell). With this command you will be able to run a shell session on your pi from your own computer. 

First connect your computer to the **Robotic-5** network. The password is the school followed by team number all lowercase one word. The pis automatically connect to this network (Thanks, Jerry). Once your computer
is on the network too you can go ahead and type the following into a terminal session. Use the number of your pi for *XX*.

```ssh pi@choate-robotics-rpi-XX.local```

You will be asked for a password. The password is ```raspberryXX``` where the *XX* stands for the pi that your are using. As you type the password the cursor will not move. **DON'T FREAK OUT**. It is fine.

## In the pi

Once in the pi, we will start to put some code to run the robot.

Your goal is to get motor running. To do this you will need work on the 
wiring. Use the little card with the pin information to set up the 
wiring to your motor controller.

Then in the terminal type: ```python3```. 

We will use the python programming language to give commands to the pi.
A few things to remember about python.

* No semi-colons.
* No braces. Instead ifs and for loops are followed by a colon, and 
then indention is used to determine the end of the loop.

The other thing about python that is kinda neat is that it is an interpreted
language meaning that we can type commands on the fly instead of writing all 
the code and then running it. That is what you are in right now. 

So let's type some code!

```
from gpiozero import PWMOutputDevice, DigitalOutputDevice
```
This is like an ```include``` in Arduino, but more specific. Instead of 
including an entire library we are including a few function from that library.

Now let's make connections (like pinMode).

![pinout for the pi](https://github.com/mbardoe/rasppirobot/blob/master/assets/pipinout.jpg)


```
enable1=PWMOutputDevice(5)
forward1=DigitalOutputDevice(6)
backward1=DigitalOutputDevice(13)
```
Your numbers maybe different

Then let's make it go.

```
forward1.on()
backward1.off()
enable1.value=.75
```

### Nano to make a file

Still you might want to make a file that can be run.

```
quit()
```
will get you out of python3. Then type the following to create folder
for your projects.

```
mkdir Robots
```
then

```
cd Robots
```
to change to that directory. If you are enjoying the whole git thing you
could ```git init``` at this point. 

Now type:

```
nano motor1.py
```

```nano``` is a simple line editor that can be run inside a shell program. 
In this program write:

```
from gpiozero import PWMOutputDevice, DigitalOutputDevice

enable1=PWMOutputDevice(5)
forward1=DigitalOutputDevice(6)
backward1=DigitalOutputDevice(13)
enable2=PWMOutputDevice(22)
forward2=DigitalOutputDevice(27)
backward2=DigitalOutputDevice(17)
forward2.on()
backward2.off()
enable2.value=.75
forward1.on()
backward1.off()
enable1.value=.75
while True:
    pass
```
You may need to update the pins to reflect your wiring. 

Then type CTRL-X to indicate that you want to save and exit. 

Once there you could type:

```
python3 motor1.py
```
to run your code.
