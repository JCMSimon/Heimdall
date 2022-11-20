import toml
from src.Logger import Logger
from random import randint

class Proxy:
	def __init__(self,debug=True) -> None:
		self.logger = Logger("Proxy",debug=debug)
		self.config = "config.toml"
		self.loadConfig()
		self.used = []

	def loadConfig(self):
		with open(self.config,"r") as file:
			self.proxyfile = toml.load(self.config,)["PROXYLIST"]["file"]
		with open(self.proxyfile) as file:
			self.proxyList = file.read().splitlines()

	def getProxy(self,unused=False):
		if unused:
			list = [proxy for proxy in self.proxyList if proxy not in self.used]
			try:
				proxy = list[randint(0,len(list) - 1)]
				self.used.append(proxy)
				return proxy
			except (IndexError,ValueError):
				self.logger.infoMsg("No unused proxy left!")
				return None
		else:
			try:
				proxy = self.proxyList[randint(0,len(self.proxyList) - 1)]
				return proxy
			except IndexError:
				self.logger.infoMsg("No proxies found!")

