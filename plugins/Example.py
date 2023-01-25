from plugins.lib.Plugin import Plugin
from plugins.lib.Data import datapoints as dp
from plugins.lib.Node import Node

class Example(Plugin):                # Class Name must be the same as the File Name
	def __init__(self,debug) -> None:
		self.debug = debug
		super().__init__(debug=self.debug,display=True,)

	def getDisplayName(self) -> str:
		return "Example Plugin"

	def getVersion(self) -> str:
		return "0.0.1"

	def accepts(self):
		return [dp.name.first_name]

	def run(self,arg) -> list:
		testResult = Node("Example Result",debug=self.debug)
		testResult.addDataField(dp.hashes.generic,"RXhhbXBsZQ==")
		return [testResult]