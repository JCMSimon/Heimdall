from turtle import onclick, width
import dearpygui.dearpygui as dpg

class GUI:
	def __init__(self) -> None:
		# Gui-Config ##########
		self.width,self.height = 1100,600
		# plugin Stuff ########
		#TODO Init Plugin Handler here
		# Gui Stuff ###########
		dpg.create_context()
		dpg.create_viewport(
			clear_color=(111,111,111,255),
			resizable=False,
			decorated=False,
			height=self.height,
			width=self.width
			)
		dpg.setup_dearpygui()
		dpg.show_viewport()
		self.initMainWindow()
		self.start()

	def initMainWindow(self):
		#Main Window (Wrapper)
		with dpg.window(horizontal_scrollbar=False, no_background=True, no_scrollbar=True, no_collapse=True, no_resize=True, menubar=False, no_close=True, no_move=True, tag="mainWindow"):
			with dpg.theme() as mainWindowTheme:
				with dpg.font_registry():
					titleFont = dpg.add_font("assets/Arial.ttf", 25)
					searchUIFont = dpg.add_font("assets/Arial.ttf", 16)
				with dpg.theme_component():
					dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive,(90,0,170,100))
					dpg.add_theme_color(dpg.mvThemeCol_TitleBg,(90,0,170,100))
					dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed,(90,0,170,100))
					dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign,0.5,0.5)
					dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
					dpg.bind_theme(mainWindowTheme)
					dpg.bind_font(titleFont)
			with dpg.handler_registry():
				dpg.add_mouse_drag_handler(button=0, threshold=0.0, callback=self.drag)

			#Node Editor Window
			with dpg.window(horizontal_scrollbar=False, no_scrollbar=True, no_collapse=True, no_resize=True, menubar=False, no_title_bar=False, no_close=False, no_move=True, height = int(self.height / 100 * 65), width=self.width - 10, tag="nodeWindow", label="Heimdall", on_close=self.exit):
				pass

			#Search Window
			with dpg.window(horizontal_scrollbar=False, no_scrollbar=True, no_collapse=True, no_resize=True, menubar=False, no_title_bar=False, no_close=True, no_move=True, pos = [0, int(self.height / 100 * 65)], height = int(self.height / 100 * 35), width= self.width, tag="searchWindow", label="Search") as window:
				dpg.bind_item_font(window,searchUIFont)
				pass
			# with dpg.font_registry():
			# with dpg.theme as searchUITheme:
			# 	with dpg.theme_component():
			# 		# dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
			# 		dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive,(111,111,111,100))
			# 		dpg.add_theme_color(dpg.mvThemeCol_TitleBg,(111,111,111,100))
			# 		dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed,(111,111,111,100))
			# 		dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign,0.5,0.5)
			# 		dpg.bind_theme(searchUITheme)
			# 		dpg.bind_font(searchUIFont)


		dpg.set_primary_window("mainWindow", True)

	def start(self):
		dpg.start_dearpygui()

	def exit(self):
		dpg.destroy_context()


	#Thanks to https://github.com/bandit-masked
	def drag(self,sender, app_data, user_data):
		if dpg.get_mouse_pos(local=False)[1] < 40:  # only drag the viewport when dragging the logo
			drag_deltas = app_data
			viewport_current_pos = dpg.get_viewport_pos()
			new_x_position = viewport_current_pos[0] + drag_deltas[1]
			new_y_position = viewport_current_pos[1] + drag_deltas[2]
			new_y_position = max(new_y_position, 0) # prevent the viewport to go off the top of the screen
			dpg.set_viewport_pos([new_x_position, new_y_position])



	# def initSearchGui(self):
	# 	height = int(self.height / 10 * 3)
	# 	with dpg.window(
	# 		horizontal_scrollbar=False,
	# 		no_background=False,
	# 		no_title_bar=False,
	# 		no_scrollbar=True,
	# 		no_collapse=False,
	# 		no_resize=True,
	# 		menubar=True,
	# 		no_close=True,
	# 		no_move=True,
	# 		tag="searchGuiWindow",
	# 		height=height,
	# 		width=self.width,
	# 		pos=(0,0),
	# 			):
	# 		with dpg.handler_registry():
	# 			dpg.add_mouse_drag_handler(button=0, threshold=0.0, callback=self.drag)
	# 		self.typeSelector = dpg.add_combo(
	# 			items=("Email", "Image", "Name", "Phone Number", "Username",),
	# 			tag="searchGuiTypeSelector",
	# 			default_value="Username",
	# 			no_arrow_button=True,
	# 			enabled=True
				# )
				# self.searchBar = dpg.add_input_text(
				# 	pos=[int(((self.width - self.typeSelectorWidth)/100*20) + self.typeSelectorWidth),int(self.height / 2 - self.searchBarFontSize)],
				# 	tag="searchGuiSearchBar",
				# 	height=self.searchBarFontSize,
				# 	width=self.searchBarWidth,
				# 	hint="Search for anything...",
				# 	)

	# def initCustomThemes(self):
	# 	with dpg.font_registry():
	# 		typeSelectorFont = dpg.add_font("assets/Arial.ttf", 25)
	# 		# searchBarFont = dpg.add_font("assets/Arial.ttf", self.searchBarFontSize)
	# 	with dpg.theme() as typeSelectorTheme:
	# 		with dpg.theme_component(dpg.mvAll):
	# 			dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize,0)
	# 			dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing,0)
	# 			dpg.add_theme_style(dpg.mvStyleVar_FramePadding,0,0)
	# 			dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0)
	# 			dpg.add_theme_style(dpg.mvStyleVar_SelectableTextAlign,0.5,0)
	# 			dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign,0.5,0)
	# 			dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered,(60,0,140,255))
	# 			dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered,(60,0,140,100))
	# 			dpg.add_theme_color(dpg.mvThemeCol_HeaderActive,(90,0,165,100))
	# 	# with dpg.theme() as searchBarTheme:
	# 	# 	with dpg.theme_component(dpg.mvAll):
	# 	# 		dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing,0)
	# 	# 		dpg.add_theme_style(dpg.mvStyleVar_FramePadding,0,0)
	# 	# 		dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0)
	# 	dpg.bind_item_theme(self.typeSelector, typeSelectorTheme)
	# 	dpg.bind_item_font(self.typeSelector, typeSelectorFont)
	# 	# dpg.bind_item_theme(self.searchBar, searchBarTheme)
	# 	# dpg.bind_item_font(self.searchBar, searchBarFont)
		# dpg.window

Heimdall = GUI()

