from time import localtime

from colorama import Fore, Style
from colorama import init as initColors


class Logger():
	"""
	Logging Utility for Heimdall
	"""
	def __init__(self,PREFIX,DEBUG=False) -> None:
		"""
		This method initialises a Heimdall Logger Instance

		Args:
		  PREFIX: This is the prefix that will be used for all messages.
		  DEBUG: If set to True, the logger will print debug messages. Defaults to False
		"""
		self._DEBUG = DEBUG
		self._PREFIX = PREFIX
		# This method initialises colorama colors
		initColors()

	def debugMsg(self,text) -> None:
		if self._DEBUG:
			print(f"{Fore.BLUE}[?] [{self.getTimeStamp()} - DEBUG]> ({self._PREFIX}) {text}{Style.RESET_ALL}")

	def infoMsg(self,text) -> None:
		print(f"{Fore.CYAN}[i] [{self.getTimeStamp()} - INFO ]> ({self._PREFIX}) {text}{Style.RESET_ALL}")

	def warnMsg(self,text) -> None:
		print(f"{Fore.YELLOW}[!] [{self.getTimeStamp()} - WARN ] > ({self._PREFIX}) {text}{Style.RESET_ALL}")

	def errorMsg(self,text) -> None:
		print(f"{Fore.RED}[x] [{self.getTimeStamp()} - ERROR]> ({self._PREFIX}) {text}{Style.RESET_ALL}")

	def getTimeStamp(self) -> str:
		"""
		It returns a string in the format of HH:MM:SS (24 Hour Format)

		Returns:
		  A string in the format of HH:MM:SS
		"""
		lt = localtime()
		# These 3 line make sure it displays 05:05:05 instead of 5:5:5 (Propper 24 Hour Format)
		hour = lt.tm_hour if str((lt.tm_hour)) == 2 else f"0{lt.tm_hour}"
		minute = lt.tm_min if str((lt.tm_min)) == 2 else f"0{lt.tm_min}"
		second = lt.tm_sec if str((lt.tm_sec)) == 2 else f"0{lt.tm_sec}"
		return ":".join([hour,minute,second])