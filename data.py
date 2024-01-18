class Data:
	def __init__(self):
		# cell values, used for creating the CAN messages simulating the battery CAN
		self.temperature = 20
		self.hex_temperature = 14
		self.voltage = 4000
		self.hex_voltage = 0xA00F

		# flags and data used for handling the 
		self.can_name = "vcan0"
		self.mode_select = 0
		self.print_mode = 0
		self.send_mode = 0

	# under are just getters and setters for the variables above
	def get_temperature(self):
		return self.temperature

	def set_temperature(self, value):
		self.temperature = value

	def get_voltage(self):
		return self.voltage

	def set_voltage(self, value):
		self.voltage = value
		self.hex_voltage = ((self.voltage & 0xFF00) >> 8) | ((self.voltage & 0x00FF) << 8)

	def get_hex_temperature(self):
		return self.hex_temperature

	def get_hex_voltage(self):
		return self.hex_voltage

	def get_can_name(self):
		return self.can_name

	def set_can_name(self, value):
		self.can_name = value

	def get_mode_select(self):
		return self.mode_select

	def set_mode_select(self, value):
		self.mode_select = value

	def get_print_mode(self):
		return self.print_mode

	def set_print_mode(self, value):
		self.print_mode = value

	def get_send_mode(self):
		return self.send_mode

	def set_send_mode(self, value):
		self.send_mode = value