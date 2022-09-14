from colorama import Fore,Style,init

class Logger():
	def __init__(self,prefix) -> None:
		self.prefix = prefix
		init()

	def debug(self,text,debug = False):
		if debug:
			print(f"{Fore.BLUE}[{self.prefix} - DEBUG] {text}{Style.RESET_ALL}")

	def info(self,text):
			print(f"{Fore.CYAN}[{self.prefix} - INFO] {text}{Style.RESET_ALL}")

	def warn(self,text):
			print(f"{Fore.YELLOW}[{self.prefix} - WARN] {text}{Style.RESET_ALL}")

	def error(self,text):
			print(f"{Fore.RED}[{self.prefix} - ERROR] {text}{Style.RESET_ALL}")

if __name__ == "__main__":
	class Example():
		def __init__(self,debug) -> None:
			logger = Logger("Test")
			logger.debug("Testing Debug Message",debug)
			logger.info("Testing Info Message")
			logger.warn("Testing Warn Message")
			logger.error("Testing Error Message")
	print("Debug turned off:")
	debugOff = Example(False)
	print("Debug turned on:")
	debugOn = Example(True)
