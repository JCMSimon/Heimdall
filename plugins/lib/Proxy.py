#TODO This needs a rework. it shouldnt only return a string form a file but rather
#     return a proxy that is 100% working and also returns its type

from random import choice

import toml

from src.Logger import Logger


class Proxy:
	def __init__(self,DEBUG=True) -> None:
		self.logger = Logger("Proxy",DEBUG=DEBUG)
		self.configFile = "config.toml"
		self.loadConfig()
		self.used = []

	def loadConfig(self) -> None:
		with open(self.configFile,"r") as file:
			self.proxyfile = toml.load(self.configFile,)["PROXYLIST"]["file"]
		try:
			with open(self.proxyfile) as file:
				self.proxyList = file.read().splitlines()
		except FileNotFoundError:
			self.logger.warnMsg(f"Proxylist {self.proxyfile} not found!")
			self.proxyList = []

	def getProxy(self,unused=False) -> str | None:
		if self.proxyList:
			if unused:
				try:
					proxy = choice([proxy for proxy in self.proxyList if proxy not in self.used])
					self.used.append(proxy)
					return proxy
				except IndexError:
					self.logger.infoMsg("No unused proxy left!")
					return None
			else:
				try:
					return choice(self.proxyList)
				except IndexError:
					self.logger.infoMsg("No proxies found!")
		else:
			self.logger.warnMsg("Proxylist empty!")
			return None

