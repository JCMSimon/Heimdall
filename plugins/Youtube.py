from plugins.lib.Plugin import Plugin
from plugins.lib.Data import datapoints as dp
from plugins.lib.Node import Node

class Youtube(Plugin):                # Class Name must be the same as the File Name
	def __init__(self,debug) -> None:
		self.debug = debug
		super().__init__(debug=self.debug,display=True)

	def getDisplayName(self) -> str:
		return "Facebook Name Plugin"

	def getVersion(self) -> str:
		return "0.0.1"

	def accepts(self):
		#accepts a birthplace address or gmail
		return [dp.username.instagram]

	def run(self,arg) -> list:
		testResult = Node("Youtube Username",debug=self.debug)
		testResult.addDataField(dp.username.youtube,"JustCallMeSimon_")
		return [testResult]