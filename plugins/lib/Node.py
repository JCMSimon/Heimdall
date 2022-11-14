from src.Logger import Logger

class Node():
	def __init__(self,title,debug=False) -> None:
		self.logger = Logger(f"Node({title})",debug=debug)
		self.data = {
			"title":title,
			"data":[],
			"image":None,
		}

	def addDataField(self,datatype,data):
		self.data["data"].append({datatype:data})

	def removeDataField(self,datatype,data):
		self.data["data"].remove({datatype:data})

	def addImage(imagetype,imageUrl):
		pass

	# def printData(self):
	# 	self.logger.debugMsg("##########")
	# 	self.logger.debugMsg(self.data["title"])
	# 	self.logger.debugMsg("##########")
	# 	for datatype,data in self.data["data"].items():
	# 		self.logger.debugMsg(f"{datatype}:{data}")
	# 	self.logger.debugMsg(f"Image: {self.data["image"]}")