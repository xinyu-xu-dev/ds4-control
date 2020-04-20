#!/usr/bin/env python3

import smbus

i2c_ch = 1
i2c_address = 41

reg_joystick_left_X = 0
reg_joystick_left_Y = 1
reg_joystick_right_X = 2
reg_joystick_right_Y = 3
reg_accelerometer_X = 4
reg_accelerometer_Y = 5
reg_L2 = 6
reg_R2 = 7
reg_touchpad_X = 11
reg_touchpad_Y = 12
reg_battery_level = 13

bus = smbus.SMBus(i2c_ch)


dic_ds4_properies = {
    'Left Joystick X': [0, -1],
    'Left Joystick Y': [1, -1],
    'Right Joystick X': [2, -1],
    'Right Joystick Y': [3, -1],
    'Accelerometer X': [4, -1],
    'Accelerometer Y': [5, -1],
    'L2': [6, -1],
    'R2': [7, -1],
    'Compas Value': [8, -1],
    'Button Square': [8, 4],
    'Button Cross': [8, 5],
    'Button Circle': [8, 6],
    'Button Triangle': [8, 7],
    'Button L1': [9, 0],
    'Button R1': [9, 1],
    'Button L2': [9, 2],
    'Button R2': [9, 3],
    'Button Share': [9, 4],
    'Button Options': [9, 5],
    'Button L3': [9, 6],
    'Button R3': [9, 7],
    'Button PS4': [10, 0],
    'Button Touchpad': [10, 0],
    'Touchpad X': [11, -1],
    'Touchpad Y': [12, -1],
    'Battery Level': [13, -1]
    }
