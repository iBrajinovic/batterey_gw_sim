#!/bin/bash
temperature=59
voltage=18445
while :
do
	cansend can0 `printf "501#%04X%04X%04X%04X\n" $voltage $voltage $voltage $voltage`
	cansend can0 `printf "502#%04X%04X%04X%04X\n" $voltage $voltage $voltage $voltage`
	cansend can0 `printf "503#%04X%04X00000000\n" $voltage $voltage`
	cansend can0 `printf "601#%02X%02X%02X%02X%02X%02X%02X%02X\n" $temperature $temperature $temperature $temperature $temperature $temperature $temperature $temperature`
	cansend can0 401#AC00000000064A10
	cansend can0 `printf "602#%02X%02X%02X%02X%02X%02X0000\n" $temperature $temperature $temperature $temperature $temperature $temperature`
done
