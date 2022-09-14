from abc import ABC,abstractmethod
from Logger import Logger
class Plugin(ABC):
	"""
	Base for all Plugins

	Args:
		debug (bool): decides if debug info is given or not
	"""
	def __init__(self,debug) -> None:
		self.logger = Logger(f"[{self.getDisplayName()}]")
		super().__init__()

	def debugMsg(self,text,debug):
		self.logger.debug(text,debug)

	def infoMsg(self,text):
		self.logger.info(text)

	def warnMsg(self,text):
		self.logger.warn(text)

	def errorMsg(self,text):
		self.logger.error(text)

	def checkUpdate(self):
		print(f"Plugin with Name '{self.getDisplayName()}' has no update check.")

	@abstractmethod
	def getDisplayName() -> str:
		"""
		Returns Plugin Name as String

		Returns:
			str: Plugin Name
		"""

	@abstractmethod
	def getVersion() -> str:
		"""
		Returns Plugin Version as String

		Returns:
			str: Plugin Version
		"""

	@abstractmethod
	def run() -> list:
		"""
		Main Processing Method of Plugin

		Returns:
			list: List of results
		"""