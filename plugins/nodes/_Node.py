from abc import ABC,abstractmethod
from lib.Logger import Logger

class Node(ABC):
	"""
	Base for all Nodes

	Args:
		debug (bool): decides if debug info is given or not
	"""
	def __init__(self,debug) -> None:
		self.logger = Logger(f"Node System")
		self.nodeType = self.getNodeType()
		self.logger.info(f"Node of Type {self.nodeType} Created")
		super().__init__()

	@abstractmethod
	def register(self,*kwargs) -> None:
		"""
		Used to register "self.values"
		"""

	@abstractmethod
	def getNodeType(self) -> str:
		"""
		Returns Node type as String

		Returns:
			str: Node type
		"""

	@abstractmethod
	def returnInfo() -> dict:
		"""
		Returns a dictionary with all Values

		Help:
		{
			"title":["This is line 1","This is line 2"],
			"text":["This is line 1","This is line 2"],
			"image":"https://imgur.com/example.png"
		}
		"""

