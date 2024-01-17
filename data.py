class Data:
	def __init__(self):
		self.temperature = 20
		self.hex_temperature = 14
		self.voltage = 4000
		self.hex_voltage = 0xA00F

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