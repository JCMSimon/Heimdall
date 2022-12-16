from colorama import Fore,Style
from colorama import init as initColors
from time import localtime

class Logger():
	"""
	Logging Utility for Plugins
	"""
	def __init__(self,prefix,debug=False) -> None:
		"""
		This function initializes the class with the prefix and debug variables

		Args:
		  prefix: The prefix of the logger.
		  debug: If set to True, it will print out the debug messages. Defaults to False
		"""
		self._debug = debug
		self.prefix = prefix
		initColors()

	def debugMsg(self,text):
		"""
		It prints a message to the console if the debug flag is set to true

		Args:
		  text: The text to be printed
		"""
		if self._debug:
			print(f"{Fore.BLUE}[{self.getTimeStamp()} - {self.prefix} - DEBUG] {text}{Style.RESET_ALL}")

	def infoMsg(self,text):
		"""
		It prints a message in cyan to the console with a timestamp and a prefix

		Args:
		  text: The text to be printed
		"""
		print(f"{Fore.CYAN}[{self.getTimeStamp()} - {self.prefix} - INFO] {text}{Style.RESET_ALL}")

	def warnMsg(self,text):
		"""
		It prints a message in yellow with the timestamp and prefix

		Args:
		  text: The text to be printed
		"""
		print(f"{Fore.YELLOW}[{self.getTimeStamp()} - {self.prefix} - WARN] {text}{Style.RESET_ALL}")

	def errorMsg(self,text):
		"""
		It prints a red error message to the console

		Args:
		  text: The text to be printed
		"""
		print(f"{Fore.RED}[{self.getTimeStamp()} - {self.prefix} - ERROR] {text}{Style.RESET_ALL}")

	def getTimeStamp(self):
		"""
		It returns the current time in the format of HH:MM:SS

		Returns:
		  The current time in the format of HH:MM:SS
		"""
		if len(str(localtime().tm_hour)) == 1:
			hour = f"0{localtime().tm_hour}"
		else:
			hour = localtime().tm_hour
		return f"{hour}:{localtime().tm_min}:{localtime().tm_sec}"