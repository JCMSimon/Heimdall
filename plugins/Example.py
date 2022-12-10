from plugins.lib.Plugin import Plugin
from plugins.lib.Data import datapoints as dp
from plugins.lib.Node import Node
from src.APIRegister import APIRegister

class Example(Plugin):                # Class Name must be the same as the File Name
	def __init__(self,debug) -> None:
		self.debug = debug
		super().__init__(debug=self.debug,display=True)

	def getDisplayName(self) -> str:
		return "Example Plugin" # This shouldnt be a name but rather the input that is wanted. ex: Username

	def getVersion(self) -> str:
		return "0.0.1"

	def accepts(self):
		#accepts a birthplace address or gmail
		return [dp.birth_place.address.address,dp.email.gmail]

	def run(self,arg) -> list:
		self.logger.infoMsg("""
	Every Plugin has access to self.logger.

		You can use it to print Info,debug,warning and error Messages specific to your Plugin
		Be sure to use debug Messages only for actual debug Info as it wont be shown without the --debug tag

	Your Plugin Name in the Selection will be the same as the file name (Username.py -> Username)

	Methods:
		getDisplayName:
		simply return a Name to be used by the Logger.

		getVersion:
		simply return a string with usual version info (0.2.5)
		(unused atm)

		run:
		this is where you will get the input as a aegument. for example a email.
		this is also where you process that info and return Nodes (explained in a bit)

		accepts:
		this is where you define what kinds of data your plugin can process (gmail,generic email,image of face)
		if the plugin does not accept any input after the initial run simply put 'dp.undefined'

		optionally you can include a 'CheckUpdate' method.
		you can use it to tell the user how to update your plugin or do it automatically if you so desire.

	Node System
		After processing the input you should return the results as a List of Nodes.
		Lets say you get a email as input and 2 Usernames as output.
		The Code would look smth like this

		username1 = Node("Youtube Username",debug=self.debug)
		username1.addDataField(dp.username.youtube,"YoutubeGamer597")
		username2 = Node("Instagram Username",debug=self.debug)
		username2.addDataField(dp.username.instagram,"InstagramGamer996")

		if you want to show a Image in your Result simply do:
		username2.addImage(dp.image.generic,"https://pbs.twimg.com/profile_images/1270048477205200908/yS0f43oV_400x400.jpg")

	You also Have Access to Tools. Simply import them like this:
	Tools will include smth like NameMC lookup,nmap etc

		from plugins.tools.ExampleTool import doSomething

	If for some reason you want to address a API directly, you can request a API Key from the config like this:

		OLD#OLD#OLD#OLD#OLD
		apiKeys = KeyRegister(apiKeys=["Dehashed","SkidSearch","SomeOtherSupportedPlatform"])
		OLD#OLD#OLD#OLD#OLD
""")
		testResult = Node("Discord Username",debug=self.debug)
		testResult.addDataField(dp.username.pinterest,"JCMS")
		testResult2 = Node("Youtube Username",debug=self.debug)
		testResult2.addDataField(dp.username.youtube,"JCMS_")
		imageResult = Node("Youtube Username",debug=self.debug)
		imageResult.addDataField(dp.username.instagram,"JCMS")
		imageResult.addDataField(dp.body.eye_color,"blue")
		imageResult.addImage(dp.image.generic,"https://pbs.twimg.com/profile_images/1270048477205200908/yS0f43oV_400x400.jpg")
		return [testResult] * 100