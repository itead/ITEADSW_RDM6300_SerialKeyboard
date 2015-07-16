#! /usr/bin/env python
#coding=utf-8

import time
import serial
import win32api
import win32con

uart = serial.Serial(
    port = 'COM10',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

def keybdUpper(val):
	if (val >= 65 and val <= 90):
		win32api.keybd_event(16,0,0,0)
		win32api.keybd_event(val,0,0,0)
		win32api.keybd_event(val,0,win32con.KEYEVENTF_KEYUP,0)
		win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)

def keybdLower(val):
	if (val >= 65 and val <= 90):
		win32api.keybd_event(val,0,0,0)
		win32api.keybd_event(val,0,win32con.KEYEVENTF_KEYUP,0)
	
def keybdNumber(val):
	if (val >= 96 and val <= 105):
		win32api.keybd_event(val,0,0,0)
		win32api.keybd_event(val,0,win32con.KEYEVENTF_KEYUP,0)

print "Waiting for data..."
while True:
	time.sleep(0.1)
	while uart.inWaiting() > 0:
		raw = uart.read(1)
		val = ord(raw)
		if (val >= 65 and val <= 90): # A - Z
			keybdUpper(val)
		elif (val >= 97 and val <= 122): # a - z
			keybdLower(val - 32)
		elif (val >= 48 and val <= 57): # 0 - 9
			keybdNumber(val + 48)
		else:
			win32api.keybd_event(106,0,0,0)  # *
			win32api.keybd_event(106,0,win32con.KEYEVENTF_KEYUP,0) # *