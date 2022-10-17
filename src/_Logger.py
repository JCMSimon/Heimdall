from colorama import Fore,Style,init

class Logger():
	def __init__(self,prefix,debug=False) -> None:
		self.debug = debug
		self.prefix = prefix
		init()

	def debugMsg(self,text):
		if self.debug:
			print(f"{Fore.BLUE}[{self.prefix} - DEBUG] {text}{Style.RESET_ALL}")

	def infoMsg(self,text):
		print(f"{Fore.CYAN}[{self.prefix} - INFO] {text}{Style.RESET_ALL}")

	def warnMsg(self,text):
		print(f"{Fore.YELLOW}[{self.prefix} - WARN] {text}{Style.RESET_ALL}")

	def errorMsg(self,text):
		print(f"{Fore.RED}[{self.prefix} - ERROR] {text}{Style.RESET_ALL}")