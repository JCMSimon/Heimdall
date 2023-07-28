from plugins._lib.Plugin import Plugin
from plugins._lib.Data import datapoints as dp
from plugins._lib.Node import Node

class Example(Plugin):                # Class Name must be the same as the File Name
	def __init__(self,DEBUG) -> None:
		self._DEBUG = DEBUG
		super().__init__(DEBUG=self._DEBUG,display=True,)

	def getCredits(self):
		return {
				"author": "JCMS", # your name or alias
				"image": "https://whatever", # Url or path to a image. can be a profile picture or specific to the plugin
				"social": "fucck.yourmom", # for ex a github link
				}

	def displayname(self) -> str:
		return "Example Plugin"

	def version(self) -> str:
		return "0.0.1"

	def accepts(self):
		return [dp.name.first_name]

	def run(self,arg) -> list:
		testResult = Node("Example Result",debug=self._DEBUG)
		testResult.addDataField(dp.hashes.generic,"RXhhbXBsZQ==")
		return [testResult]