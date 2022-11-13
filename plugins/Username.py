from plugins.lib.Plugin import Plugin
from plugins.tools.ExampleTool import doSomething

class Username(Plugin):                # Class Name must be the same as the File Name
	def __init__(self,debug) -> None:
		super().__init__(debug=debug)

	def getDisplayName(self) -> str:
		return "ExampleUsernamePlugin" # This shouldnt be a name but rather the input that is wanted. ex: Username

	def getVersion(self) -> str:
		return 0.1

	def run(self,arg) -> list:
		print("IM THE USERNAME PLUGIN")
		doSomething(arg)