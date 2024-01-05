#!/bin/bash

# About

# This script is used to fake the battery gateway connected do the AXXELLON CCU.
# Without this script, the CCU cannot be set in the DISCHARGE state as the
# Error_Ecu_Communication error would be set in the 0x181 message.

# The following functionality has been implemented in this script:
# 	- send the required CAN messages to resolve the above mentioned error
#		- i.e. 401, 501, 502, 503, 601, 602
# 	- increase or decrease the temperature of each battery cell
# 	- increase or decrease the voltage of each battery cell
#	- start/stop sending the CAN messages
# 	- start/stop printing the temperature and voltage values in the CAN messages

# Requirements

# This script uses the can-utils library, to install it run the following commands:
# 	sudo apt-get update
# 	sudo apt-get -y install can-utils

# How to use?

# If needed, edit the CAN channel you are using.

# This script has to run in the foreground, it cannot be pushed to the background.
# The way I do it is I push the candump command to the background and the run this 
# in the foreground.

# 	To set the candump command in the background use the following commands:
# 		candump can0
# 		ctrl + z
# 		bg
# The ctrl + z pushes the command to the background
# The bg command resumes the command in the background


# These are all the keyboard shortcuts implemented:
#	+	increment value
#	-	decrement value
# 	t 	toggle between the temperature and voltage values
#	s 	toggle the sending of CAN messages
#	p 	toggle the pringing of values in the terminal
# 	a 	autoset the values to a safe value(a safe value is the value that doesn't cause errors)

can_channel="vcan0"

can_temperature=14
hex_temperature=0
temperature=22

can_voltage=CC0E
hex_voltage=CE
voltage=3895

mode_select=false
print_mode=false
send_mode=true

while :
do
	read -n1 -t 0.1 input
	if [ -n "$input" ]	# if there is keypress input
	then
		if [ $input = 't' ]	# toggle the currently selected value
		then
			if [ "$mode_select" = false ]
			then
				mode_select=true
			else
				mode_select=false
			fi
			sleep 0.1

		elif [ $input = '+' ]	# increase the currently selected value
		then
			if [ "$mode_select" = false ]
			then
				voltage=`expr $voltage + 1`
				sleep 0.1
			else
				temperature=`expr $temperature + 1`
				sleep 0.1
			fi

		elif [ $input = '-' ]	# decrease the currently selected value
		then
			if [ "$mode_select" = false ]
			then
				voltage=`expr $voltage - 1`
				sleep 0.1
			else
				temperature=`expr $temperature - 1`
				sleep 0.1
			fi

		elif [ $input = 'p' ]	# toggle the print of the CAN messages
		then
			if [ "$print_mode" = false ]
			then
				print_mode=true
			else
				print_mode=false
			fi

		elif [ $input = 's' ]	# toggle the sending of the CAN messages
		then
			if [ "$send_mode" = true ]
			then
				send_mode=false
			else
				send_mode=true
			fi
		
		elif [ $input = 'a' ]
		then
			voltage=3895
			temperature=15 
		fi
	fi

	# converting to big endian
	# take the first 2 hex numbers and move them to be the last 2, 
	# the same but opposite for the lower 2 numbers
	hex_voltage=$((((voltage & 0xFF00) >> 8) | ((voltage & 0x00FF) << 8) ))

	if [ "$print_mode" = true ]
	then
		can_temperature=`printf "\t60*# %02X\n" $temperature`
		can_voltage=`printf "\t50*# %04X\n" $hex_voltage`

		echo "$can_voltage"
		echo "$can_temperature"
	fi

	if [ "$send_mode" = true ]
	then
		
		cansend `printf "%s\n" $can_channel` `printf "501#%04X%04X%04X%04X\n" $hex_voltage $hex_voltage $hex_voltage $hex_voltage`
	    cansend `printf "%s\n" $can_channel` `printf "502#%04X%04X%04X%04X\n" $hex_voltage $hex_voltage $hex_voltage $hex_voltage`
	    cansend `printf "%s\n" $can_channel` `printf "503#%04X%04X00000000\n" $hex_voltage $hex_voltage`
	    cansend `printf "%s\n" $can_channel` `printf "601#%02X%02X%02X%02X%02X%02X%02X%02X\n" $temperature $temperature $temperature $temperature $temperature $temperature $temperature $temperature`
	    cansend `printf "%s\n" $can_channel` 401#AC00000000064A10
	    cansend `printf "%s\n" $can_channel` `printf "602#%02X%02X%02X%02X%02X%02X0000\n" $temperature $temperature $temperature $temperature $temperature $temperature`
	fi

done
