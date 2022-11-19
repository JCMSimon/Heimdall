from plugins.lib.Plugin import Plugin
from plugins.lib.Data import datapoints as dp
from plugins.lib.Node import Node
from src.KeyRegister import KeyRegister

class Example2(Plugin):                # Class Name must be the same as the File Name
	def __init__(self,debug) -> None:
		self.debug = debug
		super().__init__(debug=self.debug)

	def getDisplayName(self) -> str:
		return "Example Plugin 2" # This shouldnt be a name but rather the input that is wanted. ex: Username

	def getVersion(self) -> str:
		return "0.0.1"

	def accepts(self):
		return [dp.username.discord]

	def run(self,arg) -> list:
		testResult = Node("Discord Username",debug=self.debug)
		testResult.addDataField(dp.username.discord,"JCMS#0557")
		return [testResult,testResult]