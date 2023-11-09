from plugins._lib.Plugin import Plugin
from plugins._lib.Data import datapoints as dp
from plugins._lib.Node import Node

# TODO | Abondone this and write a holehe plugin as test plugin pagman

class Example(Plugin):                # Class Name must be the same as the File Name
	def __init__(self,DEBUG) -> None:
		self._DEBUG = DEBUG
		super().__init__(DEBUG=self._DEBUG)

	def getCredits(self):
		return {
				"author": "JCMS", # your name or alias
				"image": "https://whatever", # Url or path to a image. can be a profile picture or specific to the plugin
				"social": "https://jcms.dev", # for ex a github link
				}

	def displayname(self) -> str:
		return "Example Plugin"

	def version(self) -> str:
		return "0.0.1"

	def accepts(self) -> list[str]:
		return [dp.name.first_name,dp.name.first_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name,dp.name.last_name]

	def run(self,arg) -> list:
		testResult = Node("Eye Color",debug=self._DEBUG)
		testResult.addDataField(dp.person.body.eye_color,"blue")
		testResult2 = Node("Hair Color",debug=self._DEBUG)
		testResult2.addDataField(dp.person.body.hair_color,"blonde")
		return [testResult,testResult2]