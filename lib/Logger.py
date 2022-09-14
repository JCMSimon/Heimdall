class Logger():
	def __init__(self,prefix) -> None:
		self.prefix = prefix

	def debug(self,text,debug = False):
		if debug:
			print(f"[{self.prefix} - DEBUG]")

	def info(self,text):
			print(f"[{self.prefix} - INFO]")

	def warn(self,text):
			print(f"[{self.prefix} - WARN]")

	def error(self,text):
			print(f"[{self.prefix} - ERROR]")