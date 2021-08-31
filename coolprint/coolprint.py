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
