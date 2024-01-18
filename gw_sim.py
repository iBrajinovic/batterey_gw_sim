import can
import time
from data import Data
from sender import Sender
import threading
import subprocess

class GwSimulator:
	def __init__(self):
		self.data = Data()
		self.bus = can.interface.Bus(data.get_can_name(), bustype="socketcan")
		self.sender = Sender(data, bus)
		self.key = ""


	def get_user_input(self):
		# non-blocking input that does not require ENTER at 
		# the end of input by using subprocess and bash commands
		# tried and failed:
		# 	- pygame
		#	- getch
		#	- threads
		#	- thermios
		# 	- subprocess

		proc = subprocess.Popen("read -n1 -t 0.1 input;echo $input", stdout = subprocess.PIPE, shell=True, executable="/bin/bash")
		(self.key, err) = proc.communicate()
		self.key = chr(self.key[0])


	def simulate(self):
		while True:
			key = self.get_user_input()
			if key == "t":
				if data.get_mode_select() == 0:
					data.set_mode_select(1)
				else:
					data.set_mode_select(0)

			elif key == "+":
				if data.get_mode_select() == 0:
					data.set_voltage(data.get_voltage() + 1)
				else:
					data.set_temperature(data.get_temperature() + 1)

			elif key == "z":
				if data.get_mode_select() == 0:
					data.set_voltage(data.get_voltage() + 10)
				else:
					data.set_temperature(data.get_temperature() + 10)

			elif key == "h":
				if data.get_mode_select() == 0:
					data.set_voltage(data.get_voltage() + 100)
				else:
					data.set_temperature(data.get_temperature() + 100)

			elif key == "-":
				if data.get_mode_select() == 0:
					data.set_voltage(data.get_voltage() - 1)
				else:
					data.set_temperature(data.get_temperature() - 1)

			elif key == "u":
				if data.get_mode_select() == 0:
					data.set_voltage(data.get_voltage() - 10)
				else:
					data.set_temperature(data.get_temperature() - 10)

			elif key == "j":
				if data.get_mode_select() == 0:
					data.set_voltage(data.get_voltage() - 100)
				else:
					data.set_temperature(data.get_temperature() - 100)

			elif key == "p":
				if data.get_print_mode() == 0:
					data.set_print_mode(1)
				else:
					data.set_print_mode(0)

			elif key == "s":
				if data.get_send_mode() == 0:
					data.set_send_mode(1)
				else:
					data.set_send_mode(0)

			elif key == "a":
				data.set_voltage(4000)
				data.set_temperature(20)

			elif key == "q":
				exit()

			if data.get_print_mode() == 1:
				print(f"\tVoltage: {data.get_hex_voltage()}\n\tTemperature: {data.get_temperature()}\n\n\n")

			if data.get_send_mode() == 1:
				sender.send()

			time.sleep(0.1)


if __name__ == "__main__":
	GwSimulator.simulate()
