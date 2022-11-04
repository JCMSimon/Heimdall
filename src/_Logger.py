from colorama import Fore,Style,init
from time import localtime

class Logger():
	def __init__(self,prefix,debug=False) -> None:
		self.debug = debug
		self.prefix = prefix
		init()

	def debugMsg(self,text):
		if self.debug:
			print(f"{Fore.BLUE}[{self.getTimeStamp()} - {self.prefix} - DEBUG] {text}{Style.RESET_ALL}")

	def infoMsg(self,text):
		print(f"{Fore.CYAN}[{self.getTimeStamp()} - {self.prefix} - INFO] {text}{Style.RESET_ALL}")

	def warnMsg(self,text):
		print(f"{Fore.YELLOW}[{self.getTimeStamp()} - {self.prefix} - WARN] {text}{Style.RESET_ALL}")

	def errorMsg(self,text):
		print(f"{Fore.RED}[{self.getTimeStamp()} - {self.prefix} - ERROR] {text}{Style.RESET_ALL}")

	def getTimeStamp(self):
		if len(str(localtime().tm_hour)) == 1:
			hour = f"0{localtime().tm_hour}"
		else:
			hour = localtime().tm_hour
		return f"{hour}:{localtime().tm_min}:{localtime().tm_sec}"