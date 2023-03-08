from abc import ABC, abstractmethod

from src.Logger import Logger


class Plugin(ABC):
	"""
	Base Class for all Heimdall Plugins
	"""
	def __init__(self, display=False, APIKEYS=None, DEBUG=False) -> None:
		self.logger = Logger(PREFIX=self.displayname(),DEBUG=DEBUG)
		self.display = display
		if APIKEYS and type(APIKEYS) == list or tuple:
			from plugins.lib.APIRegister import APIRegister
			self.APIKEYS = APIRegister(apiKeys=APIKEYS).returnKeys()
		elif APIKEYS:
			raise TypeError("Argument APIKEYS must be a list or tuple")
		super().__init__()

	@abstractmethod
	def displayname(self) -> str:
		"""Returns the Plugins display name which is used in the gui"""
		raise NotImplementedError(f"Plugin {self} has no name.")

	@abstractmethod
	def version(self) -> str:
		"""Returns the Plugins version. Uses semantic versioning"""
		self.logger.infoMsg(f"Plugin with Name '{self.displayname()}' has no version number.")
		return "Unknown"

	@abstractmethod
	def accepts(self) -> list:
		"""Returns the datapoints that the plugin accepts as input"""
		self.logger.debugMsg(f"Plugin with Name '{self.displayname()}' accepts no inputs. Manual execution only.")
		return []

	@abstractmethod
	def run(self) -> list:
		"""Plugin's main execution method.

		Returns a list of Heimdall Nodes with Results.
		"""
		raise NotImplementedError(f"Plugin with Name '{self.displayname()}' has no run method.")

	def update(self) -> bool:
		self.logger.infoMsg(f"Plugin with Name '{self.displayname()}' has no update check.")
		return False

	def defaultInput(self) -> str:
		self.logger.debugMsg(f"Plugin with Name '{self.displayname()}' has no default input.")
		return None
