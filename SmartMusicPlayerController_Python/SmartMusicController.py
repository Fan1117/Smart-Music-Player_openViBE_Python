"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream
import numpy as np
import time
import pyautogui as k
import os
#k = PyKeyboard()
shortcut = ['left', 'right', 'n', 'e','l']
def send(x): # counterwwl
#    k.tap_key(x)
    k.typewrite(x,'0.25')
    time.sleep(10)
# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
l = 0
while True:
    l = 0
    class_1 = []
    while l < 40:
        sample, timestamp = inlet.pull_sample()
        class_1.append(sample[0])
        l += 1
    c1 = np.mean(class_1)
    if c1 > 0.6:
        datastream = 0
    elif c1 <0.4:
        datastream = 1
    else:
        datastream = 2
    print('returned value:', shortcut[datastream])
    send(shortcut[datastream]) # player.exe 



        
        
    

    
