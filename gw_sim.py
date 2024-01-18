import can
import time
from data import Data
from sender import Sender
import threading
from getch import getch
from queue import Queue


queue = Queue()

def get_user_input():
	global queue
	while True:
		print("here")
		key = getch()
		queue.put(key)
		#time.sleep(0.1)
		if key == "q":
			exit()


def main():
	global queue
	can_name = "vcan0"

	data = Data()

	mode_select = 0
	print_mode = 0
	send_mode = 1

	bus = can.interface.Bus(can_name, bustype="socketcan")

	sender = Sender(data, bus)
	
	i_thread = threading.Thread(target=get_user_input)
	i_thread.start()

	
	while True:
		key = queue.get() if not queue.empty() else "0"
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
		#time.sleep(0.2)

		

	#incoming_message = bus.recv(1.0)


if __name__ == "__main__":
	main()
