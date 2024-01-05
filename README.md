# About

This script is used to fake the battery gateway connected do the AXXELLON CCU.
Without this script, the CCU cannot be set in the DISCHARGE state as the
Error_Ecu_Communication error would be set in the 0x181 message.

The following functionality has been implemented in this script:

- send the required CAN messages to resolve the above mentioned error i.e. 401, 501, 502, 503, 601, 602
- increase or decrease the temperature of each battery cell
- increase or decrease the voltage of each battery cell
- start/stop sending the CAN messages
- start/stop printing the temperature and voltage values in the CAN messages

# Requirements

This script uses the can-utils library, to install it run the following commands:

```
sudo apt-get update
sudo apt-get -y install can-utils
```

# Usage

If needed, edit the CAN channel you are using.

This script has to run in the foreground, it cannot be pushed to the background. 
The way I do it is I push the candump command to the background and the run this in the foreground.

To set the candump command in the background use the following commands:

```
candump can0
ctrl + z
bg
```

 The ctrl + z pushes the command to the background
 The bg command resumes the command in the background


# Keyboard shortcuts:

```
+	increment value
-	decrement value
t 	toggle between the temperature and voltage values
s 	toggle the sending of CAN messages
p 	toggle the pringing of values in the terminal
a 	autoset the values to a safe value(a safe value is the value that doesn't cause errors)
```