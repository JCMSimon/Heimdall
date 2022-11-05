from src._Logger import Logger

class Node():
	def __init__(self,title,image=False) -> None:
		"""
		Node

		Args:
			title (_type_): Title of the Node
			image (bool, string, optional): URL/Path to a image. Leave at False if no image
		"""
		self.logger = Logger("Node",debug=True)
		self.data = {
			"title":f"{title}",
			"data":[],
		}
		if image != False:
			self.data["image"] = image

	def addDataField(datatype,data):
		pass

