from src.Logger import Logger

class Node():
	"""Heimdall Node. Stores data in a organised way"""
	def __init__(self,title,color="#7800C8",debug=False) -> None:
		"""
		> initialisez a Heimdall Node

		Args:
		  title: The title of the node.
		  color: The color of the node. Defaults to #7800C8.
		  debug: If True, the logger will print out debug messages. Defaults to False
		"""
		self.logger = Logger(f"Node({title})",DEBUG=debug)
		self.data = {
			"title":title,
			"data":[],
			"image":None,
			"color":color,
		}
		self._children = []
	def addDataField(self,datapoint,data) -> None:
		"""
		> This function takes a datapoint and data as parameters and adds them to the Node as data field

		Args:
		datapoint: The type of data you're adding.
		data: The data to be added to the Node.
		"""
		self.data["data"].append({datapoint:data})

	def addImage(self,imagetype,imageUrl) -> None:
		"""
		This function adds an image to the Node

		Args:
		  imagetype: The type of image you want to add.
		  imageUrl: The URL or path of the image to be displayed. Images can be JPG and PNG formats.
		"""
		self.data["image"] = {imagetype:imageUrl}
