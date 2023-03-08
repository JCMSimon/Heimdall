from time import localtime

from colorama import Fore, Style
from colorama import init as initColors


class Logger():
	"""
	Logging Utility for Heimdall
	"""
	def __init__(self,PREFIX,DEBUG=False) -> None:
		self._DEBUG = DEBUG
		self._PREFIX = PREFIX
		# This method initialises colorama colors
		initColors()
		self.debugMsg(f"Logger instance initialised with prefix: {self._PREFIX}")

	def debugMsg(self,text) -> None:
		if self._DEBUG:
			print(f"{Fore.BLUE}[{self.getTimeStamp()} - {self._PREFIX} - DEBUG]> {text}{Style.RESET_ALL}")

	def infoMsg(self,text) -> None:
		print(f"{Fore.CYAN}[{self.getTimeStamp()} - {self._PREFIX} - INFO] > {text}{Style.RESET_ALL}")

	def warnMsg(self,text) -> None:
		print(f"{Fore.YELLOW}[{self.getTimeStamp()} - {self._PREFIX} - WARN] > {text}{Style.RESET_ALL}")

	def errorMsg(self,text) -> None:
		print(f"{Fore.RED}[{self.getTimeStamp()} - {self._PREFIX} - ERROR]> {text}{Style.RESET_ALL}")

	def getTimeStamp(self) -> str:
		lt = localtime()
		# These 3 line make sure it displays 05:05:05 instead of 5:5:5 (Propper 24 Hour Format)
		hour = str(lt.tm_hour) if len(str(lt.tm_hour)) == 2 else f"0{lt.tm_hour}"
		minute = str(lt.tm_min) if len(str(lt.tm_min)) == 2 else f"0{lt.tm_min}"
		second = str(lt.tm_sec) if len(str(lt.tm_sec)) == 2 else f"0{lt.tm_sec}"
		return ":".join([hour,minute,second])

if __name__ == "__main__":
	LoggerInstance = Logger("TEST",True)
	LoggerInstance.debugMsg(f"{LoggerInstance},{LoggerInstance.__dict__}")
	LoggerInstance.infoMsg("Test Info Message 123")
	LoggerInstance.debugMsg("Test Debug Message 123")
	LoggerInstance.warnMsg("Test Warn Message 123")
	LoggerInstance.errorMsg("Test Error Message 123")