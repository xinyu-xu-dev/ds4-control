# Raspberry Pi Setup

## Using the PL011 UART port

### Step 1 Login via terminal or desktop and shell

### Step 2 Device Tree Setting

Add device tree to /boot/config.txt to disable the bluetooth module

```bash
sudo nano /boot/config.txt
```

Add at the end of the file

```bash
dtoverlay=pi3-miniuart-bt # device tree overlay
```

### Step 3 Exit the ditor saving the changes and then

```bash
sudo reboot
```

## Disabling the Serial Console

The serial console on Raspberry Pi Streth is enabled by default. To use the UART port with serial devices you will need to disable tyhe console.

### Step 1 Edit /boot/cmdline.text file to disable the serial console

### Step 2 FInd the following text and remove it

```
console=seria10,115200
```
the text was found following at `console=tty1`

### Step 3 Exit the editor saving the changes and the mm

```
sudo reboot
```

With the serial console disabled, the UART serial port could be accessed via /dev/ttyAMA0

## I2C

```
sudo nano /etc/modprobe.d/raspi-blacklist.conf
```

```
# blcklist spi and i2c by default (many users don't need them)

blacklist spi-bcm2708
blacklist i2c-bcm2708
```

```
sudo nano /etc/modules
```

```
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
# Parameters can be specified after the module name.

i2c-dev
```

```
sudo apt install i2c-tools
sudo apt install python-smbus
sudo adduser pi i2c
sudo reboot
```

```
i2cdetect -y <i2c_ch>
```