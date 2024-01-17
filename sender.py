import can


class Sender():
	def __init__(self, data, can_bus):
		self.data = data
		self.bus = can_bus

	def send(self):
		temperature = "{:02X}".format(self.data.get_temperature())
		voltage = hex(self.data.get_hex_voltage())[2:]
		message_501 = can.Message(0, 0x501, False, data=bytes.fromhex(f'{voltage}{voltage}{voltage}{voltage}'))
		self.bus.send(message_501)
		message_502 = can.Message(0, 0x502, False, data=bytes.fromhex(f'{voltage}{voltage}{voltage}{voltage}'))
		self.bus.send(message_502)
		message_503 = can.Message(0, 0x503, False, data=bytes.fromhex(f'{voltage}{voltage}00000000'))
		self.bus.send(message_503)
		message_601 = can.Message(0, 0x601, False, data=bytes.fromhex(f'{temperature}{temperature}{temperature}{temperature}{temperature}{temperature}{temperature}{temperature}'))
		self.bus.send(message_601)
		message_602 = can.Message(0, 0x602, False, data=bytes.fromhex(f'{temperature}{temperature}{temperature}{temperature}{temperature}{temperature}0000'))
		self.bus.send(message_602)
		message_401 = can.Message(0, 0x401, False, data=bytes.fromhex('AC00000000064A10'))
		self.bus.send(message_401)