from abc import ABC,abstractmethod
from src.Logger import Logger
from plugins.lib.Data import datapoints as dp
class Plugin(ABC):
	def __init__(self,display=False,apiKeys=[],debug=False) -> None:
		self.logger = Logger(prefix=f"{self.getDisplayName()}",debug=debug)
		self.display = display
		if apiKeys:
			from APIRegister import APIRegister
			self.apiKeys = APIRegister().returnKeys(apiKeys)
		super().__init__()

	def debugMsg(self,text) -> None:
		self.logger.debugMsg(text)

	def infoMsg(self,text) -> None:
		self.logger.infoMsg(text)

	def warnMsg(self,text) -> None:
		self.logger.warnMsg(text)

	def errorMsg(self,text) -> None:
		self.logger.errorMsg(text)

	def update(self) -> bool:
		self.logger.infoMsg(f"Plugin with Name '{self.getDisplayName()}' has no update check.")
		return False

	@abstractmethod
	def getDisplayName(self) -> str:
		raise ValueError(f"Plugin {self} has no name.")

	@abstractmethod
	def getVersion(self) -> str:
		self.logger.infoMsg(f"Plugin with Name '{self.getDisplayName()}' has no version number.")

	@abstractmethod
	def accepts(self) -> None:
		pass

	@abstractmethod
	def run(self) -> list:
		raise ValueError(f"Plugin with Name '{self.getDisplayName()}' has no run method.")