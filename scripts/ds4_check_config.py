#!/usr/bin/env python3

import ds4_uart_control

ds4_uart_control.serial_comm.write('?\r'.encode())

while 1:

    received_message = ds4_uart_control.serial_comm.readline()
    print(received_message)