from abc import ABC,abstractmethod
from src.Logger import Logger
from src.KeyRegister import KeyRegister
from plugins.lib.Data import datapoints as dp
class Plugin(ABC):
	def __init__(self,apiKeys=[],debug=False) -> None:
		self.debug = debug
		self.logger = Logger(f"{self.getDisplayName()}",debug=self.debug)
		if apiKeys:
			self.apiKeys = KeyRegister(apiKeys)
		super().__init__()

	def debugMsg(self,text) -> None:
		self.logger.debugMsg(text)

	def infoMsg(self,text) -> None:
		self.logger.infoMsg(text)

	def warnMsg(self,text) -> None:
		self.logger.warnMsg(text)

	def errorMsg(self,text) -> None:
		self.logger.errorMsg(text)

	def checkUpdate(self) -> None:
		self.logger.infoMsg(f"Plugin with Name '{self.getDisplayName()}' has no update check.")

	@abstractmethod
	def getDisplayName(self) -> str:
		raise ValueError(f"Plugin {self} has no name.")

	@abstractmethod
	def getVersion(self) -> str:
		raise ValueError(f"Plugin with Name '{self.getDisplayName()}' has not defined a Version.")

	@abstractmethod
	def accepts(self) -> list:
		return [dp.none]

	@abstractmethod
	def run(self) -> list:
		raise ValueError(f"Plugin with Name '{self.getDisplayName()}' has no run method.")