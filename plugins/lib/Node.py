from src.Logger import Logger

class Node():
	def __init__(self,title) -> None:
		"""
		Node

		Args:
			title (_type_): Title of the Node
		"""
		self.logger = Logger("Node",debug=True)
		self.data = {
			"title":f"{title}",
			"data":[],
			"image":None,
		}

	def addDataField(datatype,data):
		pass

	def addImage(imagetype,imageUrl):
		pass