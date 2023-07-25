'''
The purpose of this file is to send  X_test to an STM32 Card
The ultimate goal is to test the CNN model on the nucleo card 

WARNING : DO NOT RUN THIS FILE -- It generates a new model 

'''
#Imports
import os
os.environ["BLINKA_FT232H"] = "1"
import board
import digitalio
from pyftdi.spi import SpiController
import struct
import Train_model
import time 

# Defining the CS 
cs_pin = digitalio.DigitalInOut(board.C0)
cs_pin.switch_to_output()
#cs_pin.direction = digitalio.Direction.OUTPUT

# Initialize SPI using pyftdi
spi = SpiController()
spi.configure('ftdi://ftdi:232h:1/1') 

# Set the chip select line high to start communication
cs_pin.value = True

# Open SPI bus
master = spi.get_port(cs=0)
master.set_frequency(1e6)

dataset = Train_model.X_test #shape 125 x (16,80)

data_bytes = []
for data in dataset :
    for values in data:
        data_ = []
        for value in values:
            byte_data = struct.pack('f', value)
            data_.extend(byte_data)
        data_bytes.append(bytearray(data_))

cs_pin.value = False

for i in range(dataset.shape[0]):
    # Transmit the byte array via SPI
    #cs_pin.value = False
    master.exchange(data_bytes[i], duplex=True)
    print([ "0x%02x" % b for b in data_bytes[i]])
time.sleep(1e-4)