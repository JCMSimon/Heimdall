from _Plugin import Plugin
class tset(Plugin):
	def __init__(self, debug) -> None:
		super().__init__(debug)

	def test1(self):
		print("test1")