from abc import ABC, abstractmethod

from src.Logger import Logger


class Plugin(ABC):
	"""
	Base Class for all Heimdall Plugins
	"""
	def __init__(self, display=False, APIKEYS=None, DEBUG=False) -> None:
		"""
		A template for a plugin.

		Args:
		  display: If True, the plugin will be displayed in the plugin list. Defaults to False
		  APIKEYS: A list of API keys to use for the plugin.
		  DEBUG: If set to True, will print out debug messages. Defaults to False
		"""
		self.logger = Logger(PREFIX=self.displayname(),DEBUG=DEBUG)
		self.display = display
		if APIKEYS and type(APIKEYS) == list or tuple:
			from plugins.lib.APIRegister import APIRegister
			self.APIKEYS = APIRegister(apiKeys=APIKEYS).getKeys()
		elif APIKEYS:
			raise TypeError("Argument APIKEYS must be a list or tuple")
		super().__init__()

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
		"""
		`update()` is a function that is used to update the plugin or check for updates.

		Returns:
		  The return value is a boolean value. True if update is successful. False if not
		"""
		self.logger.infoMsg(f"Plugin with Name '{self.displayname()}' has no update check.")
		return False

	def defaultInput(self) -> str | None:
		"""
		`defaultInput()` returns the default input for the plugin

		Returns:
		  The default input for the plugin.
		"""
		self.logger.debugMsg(f"Plugin with Name '{self.displayname()}' has no default input.")
		return None
