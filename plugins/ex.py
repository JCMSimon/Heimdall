from lib._Plugin import Plugin
class test(Plugin):
	def __init__(self,debug) -> None:
		super().__init__(debug=debug)

	def getDisplayName(self) -> str:
		return "ExamplePlugin" # This shouldnt be a name but rather the input that is wanted. ex: Username

	def getVersion(self) -> str:
		return 1.0

	def run(self) -> list:
		print("im doing smth")

if __name__ == "__main__":
	confirm = test(True)
	confirm.run()