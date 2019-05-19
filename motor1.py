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
