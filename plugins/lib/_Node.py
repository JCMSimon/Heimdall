from abc import ABC,abstractmethod
from src._Logger import Logger

class Node(ABC):
	"""
	Base for all Nodes

	Args:
		debug (bool): decides if debug info is given or not
	"""
	def __init__(self,debug) -> None:
		self.debug = debug
		self.logger = Logger(f"Node System",debug=self.debug)
		self.data = self.setup()
		super().__init__()

	def setup(self):
		return {
			"title":[],
			"text":[],
			"image":[None,""]
		}

	def addTitle(self, title):
		self.data["title"].append(title)

	def addText(self, text):
		self.data["text"].append(text)

	def setHasImage(self, Value):
		if Value != None and type(Value) == bool:
			self.data["image"][0] = Value
		else:
			raise ValueError("Image value of Node.data cant be unset nor None")

	def addImage(self, image):
		if self.data["image"][0]:
			self.data["image"][1] = image

	def returnInfo(self) -> dict:
		"""
		Returns a dictionary with all Values

		Image can be a Url or Local File
		Url is preferred

		Help:
		{
			"title":["This is line 1","This is line 2"],
			"text":["This is line 1","This is line 2"],
			"image":[True,"https://imgur.com/example.png"]
		}
		"""
		if self.data["image"][0] == None:
			raise ValueError("Image value of Node.data cant be unset")
		elif type(self.data["image"][0]) != dict:
			raise ValueError("Image value of Node.data must be bool")
		return self.data
