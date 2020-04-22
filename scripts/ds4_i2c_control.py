#!/usr/bin/env python3

''

import time
import smbus

i2c_ch = 1
i2c_address = 41

bus = smbus.SMBus(i2c_ch)

def get_joystick_left_X():
    val = bus.read_byte_data(i2c_address, 0)
    print('Left Joystick X: ', val)
    return val
def get_joystick_left_Y():
    val = bus.read_byte_data(i2c_address, 1)
    print('Left Joystick Y: ', val)
    return val
def get_joystick_right_X():
    val = bus.read_byte_data(i2c_address, 2)
    print('Right Joystick X: ', val)
    return val
def get_joystick_right_Y():
    val = bus.read_byte_data(i2c_address, 3)
    print('Right Joystick Y: ', val)
    return val
def get_accelerometer_X():
    val = bus.read_byte_data(i2c_address, 4)
    print('Accelerometer X: ', val)
    return val
def get_accelerometer_Y():
    val = bus.read_byte_data(i2c_address, 5)
    print('Accelerometer Y: ', val)
    return val
def get_L2():
    val = bus.read_byte_data(i2c_address, 6)
    print('L2: ', val)
    return val
def get_R2():
    val = bus.read_byte_data(i2c_address, 7)
    print('R2: ', val)
    return val
def get_touchpad_X():
    val = bus.read_byte_data(i2c_address, 11)
    print('Touchpad X: ', val)
    return val
def get_touchpad_Y():
    val = bus.read_byte_data(i2c_address, 12)
    print('Touchpad Y: ', val)
    return val
def get_battery_level():
    val = bus.read_byte_data(i2c_address, 13)
    print('Battery Level: ', val)
    return val


def get_all_input():
    get_joystick_left_X()
    get_joystick_left_Y()
    get_joystick_right_X()
    get_joystick_right_Y()
    get_accelerometer_X()
    get_accelerometer_Y()
    get_L2()
    get_R2()
    get_touchpad_X()
    get_touchpad_Y()
    get_battery_level()

if __name__ == '__main__':
    prev_time = time.time()
    while 1:
        try:
            update_time = time.time() - prev_time
            prev_time = time.time()
            print('Update time is:', update_time)
            get_all_input()
            time.sleep(0.001)
        except:
            print('Fail to Read')
