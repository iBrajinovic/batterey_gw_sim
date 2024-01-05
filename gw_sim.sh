#!/bin/bash
hex_temperature=14
temperature=22
hex_voltage=CC0E
voltage=3895
mode_select=false
input='p'
while :
do
	read -n1 -t 0.1 input
	if [ -n "$input" ]
	then
		if [ $input = 'q' ]
		then
			if [ "$mode_select" = false ]
			then
				mode_select=true
			else
				mode_select=false
			fi
			sleep 0.1
			echo "change"
		elif [ $input = 'q' ]
		then
			if [ "$mode_select" = true ]
			then
				mode_select = false
				sleep 0.1
				echo "change back"
			fi
		elif [ $input = 'w' ]
		then
			if [ "$mode_select" = false ]
			then
				voltage=`expr $voltage + 1`
				sleep 0.1
			else
				temperature=`expr $temperature + 1`
				sleep 0.1
			fi
			echo "increment"
		elif [ $input = 's' ]
		then
			if [ "$mode_select" = false ]
			then
				voltage=`expr $voltage - 1`
				sleep 0.1
			else
				temperature=`expr $temperature - 1`
				sleep 0.1
			fi
			echo "decrement"
		fi
	fi

	# hex_temperature=`printf "601#15151515151515%02X\n" $temperature`
	# hex_voltage=`printf "501#CC0ECC0ECC0E%04X\n\n\n" $voltage`

	# echo "$hex_voltage"
	# echo "$hex_temperature"
	cansend can0 `printf "501#%04X%04X%04X%04X\n" $voltage $voltage $voltage $voltage`
    cansend can0 `printf "502#%04X%04X%04X%04X\n" $voltage $voltage $voltage $voltage`
    cansend can0 `printf "503#%04X%04X00000000\n" $voltage $voltage`
    cansend can0 `printf "601#%02X%02X%02X%02X%02X%02X%02X%02X\n" $temperature $temperature $temperature $temperature $temperature $temperature $temperature $temperature`
    cansend can0 401#AC00000000064A10
    cansend can0 `printf "602#%02X%02X%02X%02X%02X%02X0000\n" $temperature $temperature $temperature $temperature $temperature $temperature`

done
