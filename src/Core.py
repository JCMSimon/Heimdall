from src.NodeInterface import NodeInterface

class Core():
	def __init__(self,pluginRegister,nodeEditor,debug=False) -> None:
		self.pluginRegister = pluginRegister
		self.nodeInterFace = NodeInterface(nodeEditor,debug=debug)

	def search(self,datatype,keyword):
		# pluginsToRun = self.pluginRegister.getPluginsForType(datatype)
		self.pluginRegister.runPlugin(datatype,keyword)
		pass