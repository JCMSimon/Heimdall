from src.plugin.Data import datapoints as dp
from src.plugin.Node import Node
from src.plugin.Plugin import Plugin

class MyExamplePlugin(Plugin):
	def __init__(self,DEBUG) -> None:
		self._DEBUG = DEBUG
		super().__init__(DEBUG=self._DEBUG)
		
	def displayname(self) -> str:
			return "Example Plugin"

	def version(self) -> str:
		return "0.0.1"

	def getCredits(self) -> dict[str, str]:
		return {
				"author": "JCMS",
				"image": "https://whatever", # Currently unused
				"social": "https://jcms.dev",
				}
	
	def accepts(self) -> set[str]:
		return {
			dp.name.first_name,
			dp.name.last_name,
			}

	def run(self,keyword) -> list:
		if len(keyword) % 2 == 0:
			testResult = Node("Eye Color",debug=self._DEBUG)
			testResult.addDataField(dp.person.body.eye_color,"blue")
		else:
			testResult = Node("Hair Color",debug=self._DEBUG)
			testResult.addDataField(dp.person.body.hair_color,"blonde")
		return [testResult]