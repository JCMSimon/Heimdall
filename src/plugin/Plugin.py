from abc import ABC, abstractmethod

from src.Logger import Logger


class Plugin(ABC):
	"""
	Base Class for all Heimdall Plugins
	"""
	def __init__(self, DEBUG=False) -> None:
		"""
		A template for a plugin.

		Args:
		  DEBUG: If set to True, will print out debug messages. Defaults to False
		"""
		self.logger = Logger(PREFIX=self.displayname(),DEBUG=DEBUG)
		super().__init__()
	
	@abstractmethod
	def displayname(self) -> str:
		"""Returns the Plugins display name which is used in the gui"""

	@abstractmethod
	def getCredits(self) -> dict:
		"""Returns a dictionary with credits for the plugin

			dict {
				author: authorname, # your name or alias
				image: imagePathURL, # Url or path to a image. can be a profile picture or specific to the plugin
				social: sociallink, # for ex a github link
			}
		"""
		
	@abstractmethod
	def version(self) -> str:
		"""Returns the Plugins version. Uses semantic versioning"""
	
	@abstractmethod
	def accepts(self) -> list:
		"""Returns the datapoints that the plugin accepts as input"""
		
	@abstractmethod
	def run(self) -> list:
		"""Plugin's main execution method.

		Returns a list of Heimdall Nodes with Results.
		"""
		
	def update(self) -> bool:
		"""
		`update()` is a function that is used to update the plugin or check for updates.

		Returns:
		  The return value is a boolean value. True if update is successful. False if not
		"""
		self.logger.infoMsg(f"Plugin with Name '{self.displayname()}' has no update check.")
		return False