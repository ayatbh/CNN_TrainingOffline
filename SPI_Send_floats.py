'''
Author  : Ayat B.

>> The purpose of this file is to send a list of floats 
>> The ultimate goal is to send test data to an STM32 Card in order to test the CNN model on the nucleo card 

'''
#Imports
import os
os.environ["BLINKA_FT232H"] = "1"
import time
from pyftdi.spi import SpiController
import struct

# Define a datum to send
data_list = [0.8323987540801155, 0.245038399256029, 0.7683179925005726, 0.8609805136274287, 0.5856080273146985, 0.5348755404622274 ]

# SPI communication protocol 
spi = SpiController(cs_count=2)
spi.configure('ftdi://ftdi:232h:1/1') 
slave = spi.get_port(cs=1, freq=10E6, mode=2)

# Printing the datum 
print("Transmit data:", data_list)

# Sending data 
while True:
    transmit_data = bytearray()
    for value in data_list:
        transmit_data.extend(struct.pack(">f", value))
    slave.exchange(transmit_data, duplex=True)
    time.sleep(0.1)


