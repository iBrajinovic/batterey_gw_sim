Working with threads is no easy task in python. The probelm I am having is that the function get_user_inpu() uses the getch() function for reading user input which is a blocking-mode input reading function and that stalls the whole execution sequence. One would think that is not a problem because that function is executing in another thread... One would be wrong. The way Python with the standard interpreter handles threads is concurrency. It means he does one thread and then switches to another. Since I have a blocking-mode input command, it blocks the whole execution!

# About

This script is used to fake the battery gateway connected to the AXXELLON CCU. The was it does this is by sending 401, 501, 502, 503, 601 and 602 messages via the CAN bus.
Without this script, the CCU cannot be set in the DISCHARGE state as the Error_Ecu_Communication error would be set in the 0x181 message.

This script enables the user to completely control the values of the cell voltages and temperatures as well as to start/stop sending the CAN messages.

The following functionality has been implemented in this script:

- increase/decrease the temperature of each battery cell
- increase/decrease the voltage of each battery cell
- start/stop sending the CAN messages
- start/stop printing the temperature and voltage values in the CAN messages

# Requirements

This script uses the can-utils library, to install it run the following commands:

```
sudo apt-get update
sudo apt-get -y install can-utils
```

# Usage

You run this script by typing its name in the terminal: `./gw_sim.sh`. The way you are going to use the script is left to you. I run the `candump` command in the background so it prints me the decoded messages in the terminal and I use the gw_sim in the foreground to change the cell voltage and temerature as needed. If you get the error *if_nametoindex: No such device*, you need to open(with a code/text editor you use) the script and edit the `can_channel` name you are using.

This script has to run in the **foreground**, it cannot be pushed to the background. 

To set the candump command in the background use the following commands:

```
candump can0
ctrl + z
bg
```

The `ctrl + z` stops and then pushes the currently running task to the background after which the `bg` command resumes the task in the background. 
After that, you run this script with `./gw_sim.sh` and now you manipulate the values with the keyboard shortcuts shown below.

# Keyboard shortcuts:

```
+	increment value
-	decrement value
t 	toggle between the temperature and voltage values
s 	toggle the sending of CAN messages
p 	toggle the pringing of values in the terminal
a 	autoset the values to a safe value(a safe value is the value that doesn't cause errors)
```
