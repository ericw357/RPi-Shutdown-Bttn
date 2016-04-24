#!/usr/bin/python

# Import the modules to send commands to the system and access GPIO pins
import RPi.GPIO as gpio
import os

#Set pin numbering
gpio.setmode(gpio.BCM)

#Set up pin 4 as an input
gpio.setup(4, gpio.IN, pull_up_down = GPIO.PUD_UP) 

# Set up an interrupt to look for pressed button
gpio.wait_for_edge(4, gpio.FALLING) 

# Shutdown
# os.system('shutdown now -h')nts here

# Reboot
os.system('reboot')
