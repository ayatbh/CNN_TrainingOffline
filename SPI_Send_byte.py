'''
    Author  : Ayat B.
    Purpose : Testing if the pc is able to send a binary code using SPI protocol
'''

import time
from pyftdi.spi import SpiController

spi = SpiController()
spi.configure('ftdi://ftdi:232h:1/1')

freq = 115200
slave = spi.get_port(cs=0, freq=freq, mode=0)

while True:
    write_buf = b'\x55'  # Binary code for 'U'
    read_buf = slave.exchange(write_buf, duplex=True)
    print(write_buf)
    time.sleep(0.1)
