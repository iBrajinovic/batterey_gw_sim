import cantools
import can
import time
import sys, select
from data import Data
from sender import Sender
from getch import getch
import pygame

def main():
	can_name = "vcan0"
	path_to_dbc = "ZSG_Battery_CAN_Axxellon_Module_M01-M01_20180420.dbc"

	data = Data()

	mode_select = 0
	print_mode = 0
	send_mode = 0

	key = ""

	bus = can.interface.Bus(can_name, bustype="socketcan")

	sender = Sender(data, bus)
	

	pygame.init()

	screen = pygame.display.set_mode((100,100), pygame.NOFRAME)
	
	while True:

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				key = pygame.key.name(event.key)

		if key == "t":
			if mode_select == 0:
				mode_select = 1
			else:
				mode_select = 0

		elif key == "+":
			if mode_select == 0:
				data.set_voltage(data.get_voltage() + 1)
			else:
				data.set_temperature(data.get_temperature() + 1)

		elif key == "z":
			if mode_select == 0:
				data.set_voltage(data.get_voltage() + 10)
			else:
				data.set_temperature(data.get_temperature() + 10)

		elif key == "h":
			if mode_select == 0:
				data.set_voltage(data.get_voltage() + 100)
			else:
				data.set_temperature(data.get_temperature() + 100)

		elif key == "-":
			if mode_select == 0:
				data.set_voltage(data.get_voltage() - 1)
			else:
				data.set_temperature(data.get_temperature() - 1)

		elif key == "u":
			if mode_select == 0:
				data.set_voltage(data.get_voltage() - 10)
			else:
				data.set_temperature(data.get_temperature() - 10)

		elif key == "j":
			if mode_select == 0:
				data.set_voltage(data.get_voltage() - 100)
			else:
				data.set_temperature(data.get_temperature() - 100)

		elif key == "p":
			if print_mode == 0:
				print_mode = 1
			else:
				print_mode = 0

		elif key == "s":
			if send_mode == 0:
				send_mode = 1
			else:
				send_mode = 0

		elif key == "a":
			data.set_voltage(4000)
			data.set_temperature(20)

		elif key == "q":
			exit()

		if print_mode == 1:
			print(f"Voltage: {data.get_hex_voltage()}\nTemperature: {data.get_temperature()}\n\n\n")

		if send_mode == 1:
			sender.send()

		key = "0"
		time.sleep(0.1)

		

	#incoming_message = bus.recv(1.0)


if __name__ == "__main__":
	main()
