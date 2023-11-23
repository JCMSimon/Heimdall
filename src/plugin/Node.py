from src.Logger import Logger

class Node():
	def __init__(self,title,debug=False) -> None:
		self.logger = Logger(f"Node({title})",DEBUG=debug)
		self.title = title
		self.datapoints = []
		self._children = []
		self.logger.debugMsg("Node created")

	def addDataField(self,datatype,value) -> None:
		self.datapoints.append({datatype:value})
		self.logger.debugMsg(f"Added datapoint '{datatype}' with value '{value}'")
		return self