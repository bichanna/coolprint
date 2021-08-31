import time

class NotAFloatError(Exception):
	""" Raised when the input value is not float """
	def __init__(self, value):
		self.message = f"'{value}' is not float"
		super().__init__(self.message)


def coolprint(input, timespan=0.05):
	if type(timespan) is not type(float()):
		raise NotAFloatError(timespan)
	
	for i in list(str(input)):
		print(i, flush=True, end="")
		time.sleep(timespan)
	print("\n", flush=True, end="")


def dullprint(input):
	print(input)


def starprint(input):
	print("*"*len(input))

def coolstarprint(input, timespan=0.05):
	if type(timespan) is not type(float()):
		raise NotAFloatError(timespan)
	
	for i in range(0, len(input)):
		print("*", flush=True, end="")
		time.sleep(timespan)
	print("\n", flush=True, end="")