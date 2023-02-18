from typing import NoReturn
import dearpygui.dearpygui as dpg
from os import walk

class GUI:
	"""
	Main Class for the GUI

	The function initializes the GUI, and sets the default data type to the first plugin in the list of
	plugins.

	Args:
		pluginNames: A list of strings that are the names of the plugins you want to use.
		debug: If True, the logger will print to the console. Defaults to False
	"""
	def __init__(self,pluginNames,debug=False) -> None:
		"""
		"""
		self.logger = Logger("GUI",debug=debug)
		self.pluginNames = pluginNames
		self.width,self.height = 1080,720
		self.dataType = self.pluginNames[0]
		self.initDPG()
		self.initDPGThemes()
		self.initMainWindow()

	def initDPG(self):
		"""
		It creates a context, a viewport, sets up DearPyGui, and shows the viewport
		"""
		dpg.create_context()
		dpg.create_viewport(
			title="Heimdall",
			clear_color=(111,111,111,255),
			large_icon="assets/icon.ico",
			small_icon="assets/icon.ico",
			decorated=False,
			resizable=False,
			vsync=True,
			height=self.height,
			width=self.width,
			)
		dpg.setup_dearpygui()
		dpg.show_viewport()

	def initDPGThemes(self):
		"""
		Setup for DPG Themes and Fonts
		"""
		with dpg.font_registry():
			self.titleFont = dpg.add_font("assets/Cousine-Regular.ttf", 30)
			self.searchFont = dpg.add_font("assets/Cousine-Regular.ttf", 20)
		with dpg.theme() as mainTheme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
				dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign,0.5,0.5)
				dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive,(90,0,170,100))
				dpg.add_theme_color(dpg.mvThemeCol_TitleBg,(90,0,170,100))
				dpg.add_theme_style(dpg.mvStyleVar_CellPadding,0,0)
				dpg.add_theme_style(dpg.mvStyleVar_FramePadding,0,0)
				dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(255,0,0,100))
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(255,0,0,255))
		with dpg.theme() as self.purpleButtonTheme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(90,0,170,255))
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(120,0,200,255))
				dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered,(90,0,170,255))
				dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered,(90,0,170,255))
				dpg.add_theme_color(dpg.mvThemeCol_HeaderActive,(120,0,200,255))
		dpg.bind_theme(mainTheme)

	def initMainWindow(self):
		"""
		Creates All the GUI Elements
		"""
		with dpg.window(
				tag="mainWindow",
				horizontal_scrollbar=False,
				no_background=True,
				no_scrollbar=True,
				no_title_bar=True,
				no_collapse=True,
				no_resize=True,
				menubar=False,
				no_close=True,
				no_move=True,
				):
			with dpg.handler_registry():   # Make dragging the Window possible
				dpg.add_mouse_drag_handler(
					callback=self.dragWindow,
					threshold=0.0,
					button=0,
					)
			# Node Editor Window (Wrapper)
			with dpg.window(
				tag="nodeWindow",
				label="Heimdall",          # This defines the actual title of the Application
				on_close=self.exitGUI,
				horizontal_scrollbar=False,
				no_title_bar=False,
				no_scrollbar=True,
				no_collapse=True,
				no_close=False,
				no_resize=True,
				menubar=False,
				no_move=True,
				# show=False, #TEMP
				height = int(self.height / 100 * 80), # Make it take up 80% of the Window Height
				width=self.width,
				) as nodeWindow:
				# Node Editor (VIS)
				self.nodeUI = dpg.add_node_editor(
					tag="NODEEDITOR",
					minimap=True,
					minimap_location=dpg.mvNodeMiniMap_Location_TopLeft
				)
				self.menubar = dpg.add_menu_bar()
				loadbutton = dpg.add_menu_item(label="Load",parent=self.menubar,callback=self.LoadButtonCallback)
				savebutton = dpg.add_menu_item(label="Save",parent=self.menubar,callback=self.SaveButtonCallback)
				exportbutton = dpg.add_menu_item(label="Export",parent=self.menubar,callback=self.openExportMenu,indent=975)
				dpg.bind_item_theme(loadbutton,self.purpleButtonTheme)
				dpg.bind_item_theme(savebutton,self.purpleButtonTheme)
				dpg.bind_item_theme(exportbutton,self.purpleButtonTheme)
			dpg.bind_item_font(nodeWindow,self.titleFont)
			#Search Window
			with dpg.window(
						tag="searchWindow",
						label="Search",
						horizontal_scrollbar=False,
						no_title_bar=False,
						no_scrollbar=False,
						no_collapse=True,
						no_resize=True,
						menubar=False,
						no_close=True,
						no_move=True,
						width=self.width,
						height=int(self.height / 100 * 20),
						pos = [
							0,                                # x Axis
							int(self.height / 100 * 80)       # y Axis
							],
						) as searchWindow:
				dpg.bind_item_font(searchWindow,self.searchFont)
				# Button to Choose what to search for (Type Selector Button)
				self.logger.debugMsg(f"Plugin Names before padding: {self.pluginNames}")
				self.typeSelector = dpg.add_combo(
					tag="searchGuiTypeSelector",
					items=centerText(self.pluginNames),
					default_value=centerText(self.pluginNames[0]),
					callback=self.typeSelectorCallback,
					no_arrow_button=True,
					width=int(self.width / 100 * 95) - 74,
					pos=[
						int(self.width / 2) - int(self.width / 100 * 95) // 2,
						int(int(int(self.height / 100 * 20) / 100 * 80) - 27),
					],
				)
				dpg.bind_item_theme(self.typeSelector,self.purpleButtonTheme)
				# reload button
				self.reloadButton = dpg.add_button(
					label="Reload",
					callback=self.reloadPlugins,
					pos=[
						int(self.width / 2)
						- int(self.width / 100 * 95) // 2
						+ int(int(self.width / 100 * 95) - 70)
						- 4,
						int(int(int(self.height / 100 * 20) / 100 * 80) - 27),
					],
				)
				dpg.bind_item_theme(self.reloadButton,self.purpleButtonTheme)
				self.logger.debugMsg("Plugin Names after padding:")
				for name in centerText(self.pluginNames):
					self.logger.debugMsg(f"{name}(EOL)")
				# Search Bar for input
				self.searchBar = dpg.add_input_text(
					hint="Search here...",
					on_enter=True,
					callback=self.searchBarCallback,
					width=int(self.width / 100 * 95) - 70,
					pos=[
						int(self.width / 2) - int(self.width / 100 * 95) // 2,
						int(int(int(self.height / 100 * 20) / 100 * 50) - 27),
					],
				)
				# Buttont to submit search
				self.submitButton = dpg.add_button(
					label="Submit",
					callback=self.searchButtonCallback,
					pos=[
						int(self.width / 2)
						- int(self.width / 100 * 95) // 2
						+ int(int(self.width / 100 * 95) - 70)
						- 4,
						int(int(int(self.height / 100 * 20) / 100 * 50) - 27),
					],
				)
				dpg.bind_item_theme(self.submitButton,self.purpleButtonTheme)
			dpg.bind_item_font(searchWindow,self.searchFont)
		dpg.set_primary_window("mainWindow", True)    # Maximize the Main Window Wrapper

	def typeSelectorCallback(self, _, app_data):
		"""
		It's a callback function that is called when the user selects a data type from the dropdown menu
		"""
		self.dataType = str(app_data).strip()
		self.logger.debugMsg(f"Selected '{self.dataType}' as data type")

	def searchButtonCallback(self, _, __):
		"""
		It takes the value of the search bar, and passes it to the searchBarCallback function

		Args:
		  _: The first parameter is the widget that called the function.
		  __: The event that triggered the callback.
		"""
		searchTerm = dpg.get_value(self.searchBar)
		self.searchBarCallback("Manual",searchTerm)

	def searchBarCallback(self, _, app_data):
		"""
		It takes the search term from the search bar, disables the search bar and submit button, sets the
		search bar to a message, and then executes the search
		"""
		searchTerm = str(app_data).strip()
		if searchTerm and searchTerm != "":
			dpg.disable_item(self.searchBar)
			dpg.disable_item(self.submitButton)
			dpg.set_value(self.searchBar,f"Processing '{searchTerm}' as {self.dataType}...")
			self.executeSearch(searchTerm)
			dpg.set_value(self.searchBar,"")
			dpg.enable_item(self.searchBar)
			dpg.enable_item(self.submitButton)

	def filePopup(self,path,extension,label="File Selector",allowNew=False) -> None:
		"""
		It creates a window with buttons that load or save files

		Args:
		  path: The path to the directory where the files are located
		  extension: The file extension of the files you want to load.
		  label: The title of the window. Defaults to File Selector
		  allowNew: If True, the user will be able to create a new file. Defaults to False
		"""
		self.FilePopupType = "save" if allowNew else "load"
		for (_, _, filenames) in walk(path):
			files = [filename for filename in filenames if filename.endswith(extension)]
			break
		if files or allowNew:
			self.fileSelector = dpg.add_window(
				label=label,
				modal=True,
				min_size=[int(self.width / 2),int(self.height / 2)],
				max_size=[int(self.width / 2 * 1.5),int(self.height / 2)],
				pos=[self.width / 2 - (self.width / 2 / 2),self.height / 2 - (self.height / 2 / 2)],
				no_collapse=True,
				no_move=True,
				no_resize=True,
				no_scrollbar=False
				)
			dpg.bind_item_font(self.fileSelector,self.titleFont)
			if allowNew:
				self.fileNameField = dpg.add_input_text(hint=centerText("New filename here",width=34),            # Text that is in the Box when nothing is typed
					on_enter=True,
					callback=self.saveToFile,
					width=self.width / 2,
					parent=self.fileSelector
				)
			for filename in files:
				button = (
					dpg.add_button(
						parent=self.fileSelector,
						label=str(filename).split(".")[0],
						width=(self.width / 2 * 0.89),
						callback=self.saveToFile,
					)
					if allowNew
					else dpg.add_button(
						parent=self.fileSelector,
						label=str(filename).split(".")[0],
						width=(self.width / 2 * 0.89),
						callback=self.loadFile,
					)
				)
				dpg.split_frame()
				deletebutton = dpg.add_button(parent=self.fileSelector,label="DEL",width=(self.width / 2 * 0.09),pos=[dpg.get_item_width(button),dpg.get_item_pos(button)[1]],callback=self.deleteFile)
		else:
			self.logger.infoMsg("No valid Files Found")

	def saveToFile(self,buttonID) -> None:
		"""
		It saves the current state of the program to a file.

		Args:
		  buttonID: The ID of the button that was clicked.
		"""
		if buttonID == self.fileNameField:
			filename = dpg.get_value(self.fileNameField)
		else:
			filename = dpg.get_item_label(buttonID)
		dpg.delete_item(self.fileSelector)
		self.core.save(filename)

	def deleteFile(self,buttonID) -> None:
		"""
		It deletes a file from the save directory

		Args:
		  buttonID: The ID of the button that was pressed.
		"""
		filename = dpg.get_item_label(buttonID - 1)
		if self.core.deleteSave(filename):
			dpg.delete_item(buttonID - 1)
			dpg.delete_item(buttonID)
			dpg.delete_item(self.fileSelector)
			dpg.split_frame()
			if self.FilePopupType == "load":
				self.LoadButtonCallback()
			else:
				self.SaveButtonCallback()

	def loadFile(self,buttonID) -> None:
		"""
		It takes the button ID of the button that was clicked, gets the label of that button, deletes the
		file selector, and then loads the file

		Args:
		  buttonID: The ID of the button that was clicked.
		"""
		filename = dpg.get_item_label(buttonID)
		dpg.delete_item(self.fileSelector)
		self.core.load(filename)

	def LoadButtonCallback(self) -> None:
		"""
		It opens a file dialog, and when the user selects a file, it loads the file and displays the
		contents in the text box
		"""
		self.filePopup("./saves",".pickle","Choose your Project File")

	def SaveButtonCallback(self) -> None:
		"""
		It creates a popup window that allows the user to choose a file from a directory, and then returns
		the file name
		"""
		self.filePopup("./saves",".pickle","Choose your Project File",allowNew=True)

	def openExportMenu(self) -> None:
		"""
		It creates a popup window with a text label and a button.
		"""
		with dpg.window(
				label="Export",
				popup=True,
				min_size=[int(self.width / 4),int(self.height / 10)],
				max_size=[int(self.width / 4 * 1.5),int(self.height / 10)],
				pos=[self.width / 2 - (self.width / 4 / 2),self.height / 2 - int(self.height / 10 / 2) ],
				no_collapse=True,
				no_move=True,
				no_resize=True,
				) as temppopup:
			dpg.add_text("Soon!",indent=100)
			okbutton = dpg.add_button(label="OK",indent=120,callback=lambda : dpg.delete_item(temppopup))
			dpg.bind_item_theme(okbutton,self.purpleButtonTheme)

	def executeSearch(self,searchTerm) -> None:
		"""
		It takes a search term, and passes it to the core.search function

		Args:
		  searchTerm: The search term to search for.
		"""
		self.core.search(self.dataType,searchTerm)

	def returnEditor(self) -> int | str:
		"""
		It returns the editor that is currently being used.

		Returns:
		  The nodeUI object.
		"""
		return self.nodeUI

	def reloadPlugins(self) -> None:
		"""
		It disables the search bar, submit button, reload button, and type selector, then reloads the
		plugins, then re-enables the search bar, submit button, reload button, and type selector
		"""
		items = [self.searchBar,self.submitButton,self.reloadButton,self.typeSelector]
		for item in items:
			dpg.disable_item(item)
		self.core.reloadPlugins()
		dpg.configure_item(self.typeSelector,items=centerText(self.core.pluginRegister.getPluginNames()))
		for item in items:
			dpg.enable_item(item)

	def start(self,core) -> None:
		"""
		`dpg.start_dearpygui()` is the function that starts DearPyGui.

		Args:
		  core: The core object.
		"""
		self.core = core
		dpg.start_dearpygui()

	def exitGUI(self) -> NoReturn:
		"""
		The function `exitGUI()` is called when the user clicks the "Exit" button. It destroys the context
		and exits the program
		"""
		dpg.destroy_context()
		exit(0)

	# Function to handle dragging the Window
	# Thanks to https://github.com/bandit-masked
	def dragWindow(self,sender, app_data, user_data) -> None:
		"""
		When the user drags the mouse over the Top Bar, the window moves with the mouse

		Args:
		  sender: The object that sent the event
		  app_data: The data that is passed to the callback function.
		  user_data: This is the data that you pass to the function when you register it.
		"""
		if dpg.get_mouse_pos(local=False)[1] < 40:  # only drag the viewport when dragging the logo
			drag_deltas = app_data
			if drag_deltas[0] != 0 or drag_deltas[1] != 0:
				viewport_current_pos = dpg.get_viewport_pos()
				new_x_position = viewport_current_pos[0] + drag_deltas[1]
				new_y_position = viewport_current_pos[1] + drag_deltas[2]
				new_y_position = max(new_y_position, 0) # prevent the viewport to go off the top of the screen
				self.logger.debugMsg(f"Moving Window to x:{new_x_position} y:{new_y_position} (Delta: {drag_deltas}")
				dpg.set_viewport_pos([new_x_position, new_y_position])

def centerText(itemList,width=92) -> str | list[str]:
	"""
	It takes a list of strings and centers them

	Args:
	  itemList: The list of items to be centered.
	  width: The width of the text. Defaults to 92

	Returns:
	  A list of strings that are centered.
	"""
	if type(itemList) == str:
		return f"{itemList:^{width}}"
	elif type(itemList) == list:
		itemList.sort(key=len)
		return [f"{item:^{width}}" for item in itemList]


if __name__ == "__main__":
	from Logger import Logger
	test = GUI(["tseting","tetset"],debug=True)
	test.start(None)
else:
	from src.Logger import Logger