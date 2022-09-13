from abc import ABC,abstractmethod

class Plugin(ABC):
	"""
	Base for all Plugins
	"""
	def __init__(self) -> None:
		super().__init__()

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