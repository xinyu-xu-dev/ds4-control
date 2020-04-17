#!/usr/bin/env python3

import time
import serial

command_array = ["DEVICE PS4\r", # 0
                "SERIAL ON\r", # 1
                "HEX ON\r", # 2
                "BAUD 155200\r", # 3
                "I2C 41\r", # 4
                "RGB 2155A2\r", # 5
                "?\r", # 6
                ]

ignore_command_id_array = [3, 6]

def check_device_connection_status():
    print('Looking for device...')
    start_time = time.time()
    elapsed_time = 0
    while (elapsed_time < 5):
        received_message = serial_comm.readline()
        if (len(received_message) >= 3) and (chr(received_message[0]) == 'P') and (chr(received_message[1]) == 'S') and (chr(received_message[2]) == '4'):
           print('Device Found')
           return True
        elapsed_time = time.time() - start_time
    print('No Device Found')
    return False

def send_command(id):
    if id in ignore_command_id_array:
        print('Command Ignored')
        return True
    else:
        elapsed_time = 0
        sent_byte_num = serial_comm.write(command_array[id].encode())
        command_sent_time = time.time()
        print(command_array[id])
        print("Sent {0} bytes".format(sent_byte_num))
        while (elapsed_time < 5):
            received_message = serial_comm.readline().decode('utf-8')
            elapsed_time = time.time() - command_sent_time
            if (received_message.find('Changed') >= 0):
                print('Command Acknowledged')
                return True
            if (received_message.find('Unsupported') >= 0):
                print('Command Unsupported')
                return True
        print('Timeout')
        return False

def validate(string):
    crc = 0x00
    sum = 0x00
    string_length = len(string) - 3
    if string_length >= 15:
        extract_index = 0
        while (extract_index < string_length):
            extract_char = string[extract_index]
            extract_index += 1
            bit_index = 8
            while (bit_index > 0):
                sum = (crc ^ extract_char) & 0x01
                crc = crc >> 1
                if sum:
                    crc = crc ^ 0x8C
                extract_char = extract_char >> 1
                bit_index -= 1
        print('CRC: {0}'.format(crc))
        if crc == string[string_length]:
            print('Validation Successful')
            return True
        else:
            print('Validation Failed')
            return False
    else:
        print('Received String Not Long Enough')
        return False

serial_comm = serial.Serial(
    port = '/dev/ttyAMA0',
#    baudrate = 9600,
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

def get_joystick_left_X(string):
    print('Left Joystick X: ',string[3])
    return string[3]

def get_joystick_left_Y(string):
    print('Left Joystick Y: ', string[4])
    return string[4]

def get_joystick_right_X(string):
    print('Right Joystick X: ', string[5])
    return string[5]

def get_joystick_right_Y(string):
    print('Right Joystick Y: ', string[6])
    return string[6]

def get_accelerometer_X(string):
    print('Accelerometer X: ', string[7])
    return string[7]

def get_accelerometer_Y(string):
    print('Accelerometer Y: ', string[8])
    return string[8]

def get_L2(string):
    print('L2: ', string[9])
    return string[9]

def get_R2(string):
    print('R2: ', string[10])
    return string[10]

def get_touchpad_X(string):
    print('Touchpad X: ', string[14])
    return string[10]

def get_touchpad_Y(string):
    print('Touchpad Y: ', string[15])
    return string[10]

def get_battery_level(string):
    print('Battery Level: ', string[16], '%')
    return string[10]

def get_button_status(string, button_name, byte_index, bit_index):
    b_str = bin(string[byte_index])
    len_bstr = len(b_str)
    if len_bstr >= (bit_index + 2):
        pressed = int(b_str[len_bstr - bit_index])
    else:
        pressed = False

    if pressed:
        print(button_name, ': x')
        return True
    else:
        print(button_name, ':  ')
        return False

def get_button_1(string):
    return get_button_status(string, 'Button 1', 11, 1)

def get_button_2(string):
    return get_button_status(string, 'Button 2', 11, 2)

def get_button_3(string):
    return get_button_status(string, 'Button 3', 11, 3)

def get_button_4(string):
    return get_button_status(string, 'Button 4', 11, 4)

def get_button_Square(string):
    return get_button_status(string, 'Square Button', 11, 5)

def get_button_Cross(string):
    return get_button_status(string, 'Cross Button', 11, 6)

def get_button_Circle(string):
    return get_button_status(string, 'Circle Button', 11, 7)

def get_button_Triangle(string):
    return get_button_status(string, 'Triangle Button', 11, 8)

def get_button_L1(string):
    return get_button_status(string, 'L1 Button', 12, 1)

def get_button_R1(string):
    return get_button_status(string, 'R1 Button', 12, 2)

def get_button_L2(string):
    return get_button_status(string, 'L2 Button', 12, 3)

def get_button_R2(string):
    return get_button_status(string, 'R2 Button', 12, 4)

def get_button_Share(string):
    return get_button_status(string, 'Share Button', 12, 5)

def get_button_Options(string):
    return get_button_status(string, 'Options Button', 12, 6)

def get_button_L3(string):
    return get_button_status(string, 'L3 Button', 12, 7)

def get_button_R3(string):
    return get_button_status(string, 'R3 Button', 12, 8)

def get_button_PS4(string):
    return get_button_status(string, 'PS4 Button', 13, 1)

def get_button_Touchpad(string):
    return get_button_status(string, 'Touchpad Button', 13, 2)

def get_button_compas_pad(string):
    b_str = bin(string[11])
    len_bstr = len(b_str)
    if (len_bstr >= 6):
        sb_str = b_str[len_bstr-4:len_bstr]
    else:
        sb_str = b_str[2:len_bstr]

    i_bstr = int(sb_str,2)
    lead_str = 'Compas Pad: '

    if i_bstr == 0:
        print(lead_str + 'N')
    elif i_bstr == 1:
        print(lead_str + 'NE')
    elif i_bstr == 2:
        print(lead_str +  'E')
    elif i_bstr == 3:
        print(lead_str + 'SE')
    elif i_bstr == 4:
        print(lead_str + 'S')
    elif i_bstr == 5:
        print(lead_str + 'SW')
    elif i_bstr == 6:
        print(lead_str + 'W')
    elif i_bstr == 7:
        print(lead_str + 'NW')
    elif i_bstr == 8:
        print(lead_str + 'No button pressed')

    return i_bstr

def get_button_up(compas_pad_value):
    v = compas_pad_value
    if (v == 0) or (v == 1) or (v == 7):
        print('Up Button: x')
        return True
    else:
        print('Up Button:  ')
        return False

def get_button_down(compas_pad_value):
    v = compas_pad_value
    if (v == 3) or (v == 4) or (v == 5):
        print('Down Button: x')
        return True
    else:
        print('Down Button:  ')
        return False

def get_button_left(compas_pad_value):
    v = compas_pad_value
    if (v == 5) or (v == 6) or (v == 7):
        print('Left Button: x')
        return True
    else:
        print('Left Button:  ')
        return False

def get_button_right(compas_pad_value):
    v = compas_pad_value
    if (v == 1) or (v == 2) or (v == 3):
        print('Right Button: x')
        return True
    else:
        print('Right Button:  ')
        return False

device_connected = check_device_connection_status()

if not device_connected:
    command_received = False
    while not command_received:
        command_received = send_command(0)

    serial_comm.close()
    serial_comm.open()

    send_command_id = 0

    while (send_command_id < len(command_array)):
        command_sent = send_command(send_command_id)
        send_command_id += 1

    print('USB Host has been configured successfully.')
    time.sleep(0.5)
    print('Please breifly turn on the USB Host switch and then turn it off.')
    time.sleep(0.5)
    print('After the blue LED On USB Host flash faster, press and hold the PS4 and Share buttons together on the PS4 controller until the PS4 led starts flashing.')

    while not device_connected:
        received_message = serial_comm.readline().decode('utf-8')

        if (received_message.find('Connected') >= 0):
            device_connected = True
            print('Device connected')

prevTime = time.time()

while 1:

    received_message = serial_comm.readline()
    if len(received_message) < 18:
        received_message += serial_comm.readline()
    currentTime = time.time()
    readUpdateTime = currentTime - prevTime
    prevTime = currentTime

    print("Update time is {:05.02f} ".format(readUpdateTime))
    print(received_message)

    if validate(received_message):
        get_joystick_left_X(received_message)
        get_joystick_left_Y(received_message)
        get_joystick_right_X(received_message)
        get_joystick_right_Y(received_message)
        get_accelerometer_X(received_message)
        get_accelerometer_Y(received_message)
        get_L2(received_message)
        get_R2(received_message)
        get_touchpad_X(received_message)
        get_touchpad_Y(received_message)
        get_battery_level(received_message)
        get_button_Square(received_message)
        get_button_Cross(received_message)
        get_button_Circle(received_message)
        get_button_Triangle(received_message)
        get_button_L1(received_message)
        get_button_R1(received_message)
        get_button_L2(received_message)
        get_button_R2(received_message)
        get_button_Share(received_message)
        get_button_Options(received_message)
        get_button_L3(received_message)
        get_button_R3(received_message)
        get_button_PS4(received_message)
        get_button_Touchpad(received_message)
#        get_button_1(received_message)
#        get_button_2(received_message)
#        get_button_3(received_message)
#        get_button_4(received_message)
        compas_pad_value = get_button_compas_pad(received_message)
        get_button_up(compas_pad_value)
        get_button_down(compas_pad_value)
        get_button_left(compas_pad_value)
        get_button_right(compas_pad_value)