#!/usr/bin/env python3

import serial

serial_comm = serial.Serial(
    port = '/dev/ttyAMA0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

serial_comm.write('?\r'.encode())

while 1:

    received_message = serial_comm.readline()
    print(received_message)