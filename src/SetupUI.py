import dearpygui.dearpygui as dpg
from screeninfo import get_monitors
from json import load as jsonload
from json import dump as jsondump

from src.Logger import Logger

class Setup:
	def __init__(self,debug) -> None:
		self.logger = Logger("SetupUI",DEBUG=debug)
		self.height = 230
		self.width = 280
		self.initDPG()
		self.initDPGThemes()
		self.initMainWindow()
		self.start()

	def initDPG(self):
		dpg.create_context()
		dpg.create_viewport(
			title="Setup",              # Window Title (Also Application Title)
			large_icon="assets/icon.ico",  # "favicon" for Application
			small_icon="assets/icon.ico",  # "favicon" for Application
			always_on_top=False,
			decorated=False,               # Disables Windows Bar
			resizable=False,
			height=self.height,
			width=self.width,
			x_pos = -self.width,
			y_pos = -self.height,
			)
		dpg.setup_dearpygui()
		dpg.show_viewport()
		self.centerViewport()

	def centerViewport(self):
		for monitor in get_monitors():
			if monitor.is_primary:
				monitor_xd = monitor.width
				monitor_yd = monitor.height
		dpg.set_viewport_pos(pos=[
			(monitor_xd - self.width) / 2,
			(monitor_yd - self.height) / 2,
		])

	def initDPGThemes(self):
		with dpg.font_registry():
			self.titleFont = dpg.add_font("assets/Cousine-Regular.ttf", 20)
		with dpg.theme() as self.doneButton:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(0,255,0,100))
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(0,255,0,255))
				dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0)
		with dpg.theme() as self.mainWindowStyling:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign,0.5,0.5)
				dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
				dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive,(90,0,170,100))
				dpg.add_theme_color(dpg.mvThemeCol_TitleBg,(90,0,170,100))
				dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed,(90,0,170,100))
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(255,0,0,100))
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(255,0,0,255))
				dpg.add_theme_color(dpg.mvThemeCol_CheckMark,(0,255,0,255))
				dpg.bind_theme(self.mainWindowStyling)
				dpg.bind_font(self.titleFont)

	def initMainWindow(self):
		with dpg.window(
			label="Setup",
			tag="mainWindow",
			horizontal_scrollbar=False,
			no_background=False,
			no_scrollbar=True,
			no_collapse=True,
			no_resize=True,
			menubar=False,
			no_close=False,
			on_close=self.exitGUI,
			no_move=True,
			height=self.height,
			width=self.width,
				):
			with dpg.table(header_row=False, resizable=False, tag="table",policy=dpg.mvTable_SizingFixedFit):
				dpg.add_table_column(parent="table")
				dpg.add_table_column(default_sort=True, parent="table")
				with dpg.table_row(parent="table"):
					dpg.add_text("Auto Check for update")
					self.autoCheckUpdate = dpg.add_checkbox()
				with dpg.table_row(parent="table"):
					dpg.add_text("Warn before updating")
					self.warnUpdate = dpg.add_checkbox(default_value=True)
				with dpg.table_row(parent="table"):
					dpg.add_text("Ignore major updates")
					self.majorUpdates = dpg.add_checkbox(callback=self.toggleMinorButton)
				with dpg.table_row(parent="table"):
					dpg.add_text("Ignore minor updates")
					self.minorUpdates = dpg.add_checkbox()
				with dpg.table_row(parent="table"):
					dpg.add_text("Auto Plugin Update")
					self.pluginUpdates = dpg.add_checkbox()
			doneButton = dpg.add_button(width=self.width * 0.94,label="DONE",callback=self.save)
			dpg.bind_item_theme(doneButton,self.doneButton)
			with dpg.handler_registry():   # Make dragging the Window possible
				dpg.add_mouse_drag_handler(
					callback=self.dragWindow,
					threshold=0.0,
					button=0,
			)

	# Starts GUI
	def start(self):
		dpg.start_dearpygui()

	def exitGUI(self):
		dpg.destroy_context()
		exit()

	def toggleMinorButton(self):
		if dpg.is_item_enabled(self.minorUpdates):
			dpg.disable_item(self.minorUpdates)
			dpg.set_value(self.minorUpdates,True)
		else:
			dpg.enable_item(self.minorUpdates)
			dpg.set_value(self.minorUpdates,False)


	def save(self):
		self.logger.debugMsg(f"Saving Settings:")
		self.logger.debugMsg(f"majorUpdates: {dpg.get_value(self.majorUpdates)}")
		self.logger.debugMsg(f"minorUpdates: {dpg.get_value(self.minorUpdates)}")
		self.logger.debugMsg(f"warnUpdate  : {dpg.get_value(self.warnUpdate)}")
		with open("updateconfig.json","r") as file:
			settings = jsonload(file)
		settings["ignoreMinorUpdates"] = dpg.get_value(self.minorUpdates)
		settings["ignoreMajorUpdates"] = dpg.get_value(self.majorUpdates)
		settings["ignorePreRequestWarnings"] = dpg.get_value(self.warnUpdate)
		settings["autoUpdate"] = dpg.get_value(self.autoCheckUpdate)
		if settings["autoUpdate"]:
			self.logger.infoMsg("Auto updates enabled. Restart the Application to check for updates")
		settings["oneTimeSetupDone"] = True
		with open("updateconfig.json","w") as file:
			jsondump(settings,file,indent=4)
		self.exitGUI()

	# Function to handle dragging the Window
	# Thanks to https://github.com/bandit-masked
	def dragWindow(self,sender, app_data, user_data):
		if dpg.get_mouse_pos(local=False)[1] < 40:  # only drag the viewport when dragging the logo
			drag_deltas = app_data
			if drag_deltas[0] != 0 or drag_deltas[1] != 0:
				viewport_current_pos = dpg.get_viewport_pos()
				new_x_position = viewport_current_pos[0] + drag_deltas[1]
				new_y_position = viewport_current_pos[1] + drag_deltas[2]
				new_y_position = max(new_y_position, 0) # prevent the viewport to go off the top of the screen
				self.logger.debugMsg(f"Moving Window to x:{new_x_position} y:{new_y_position} (Delta: {drag_deltas}")
				dpg.set_viewport_pos([new_x_position, new_y_position])