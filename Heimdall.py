import dearpygui.dearpygui as dpg

class SearchGUI:
	def __init__(self) -> None:
		# Gui-Config ##########
		self.width,self.height = 1100,600
		self.searchBarWidth = 570
		self.searchBarFontSize = 25 #this is in pt
		self.typeSelectorWidth = 150
		self.typeSelectorFontSize = 25 #this is in pt
		# plugin Stuff ########
		#TODO Init Plugin Handler here
		# Gui Stuff ###########
		dpg.create_context()
		dpg.create_viewport(
			clear_color=(0,0,0,255),
			resizable=False,
			decorated=True,
			vsync=True,
			height=self.height,
			width=self.width)
		dpg.setup_dearpygui()
		dpg.show_viewport()
		self.initSearchGui()
		self.initCustomThemes()
		self.start()

	def start(self):
		dpg.start_dearpygui()
		dpg.destroy_context()


	def initSearchGui(self):
		with dpg.window(
			horizontal_scrollbar=False,
			no_background=True,
			no_title_bar=True,
			no_scrollbar=True,
			no_collapse=True,
			no_resize=True,
			menubar=False,
			no_close=True,
			no_move=True,
			tag="searchGuiWindow",
			height=self.height,
			width=self.width,
			pos=(0,0)
				):
				self.typeSelector = dpg.add_combo(
					pos=[int((self.width - self.typeSelectorWidth)/100*20),int(self.height / 2 - self.typeSelectorFontSize)],
					width=self.typeSelectorWidth,
					items=("Email", "Image", "Name", "Phone Number", "Username",),
					tag="searchGuiTypeSelector",
					default_value="Username",
					no_arrow_button=True,
					enabled=True
					)
				self.searchBar = dpg.add_input_text(
					pos=[int(((self.width - self.typeSelectorWidth)/100*20) + self.typeSelectorWidth),int(self.height / 2 - self.searchBarFontSize)],
					height=self.searchBarFontSize,
					width=self.searchBarWidth,
					show=True,
					)


	def initCustomThemes(self):
		with dpg.font_registry():
			typeSelectorFont = dpg.add_font("assets/Arial.ttf", self.typeSelectorFontSize)
			searchBarFont = dpg.add_font("assets/Arial.ttf", self.searchBarFontSize)
		with dpg.theme() as typeSelectorTheme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize,0)
				dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing,0)
				dpg.add_theme_style(dpg.mvStyleVar_FramePadding,0,0)
				dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0)
				dpg.add_theme_style(dpg.mvStyleVar_SelectableTextAlign,0.5,0)
				dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign,0.5,0)
				dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered,(60,0,140,255))
				dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered,(60,0,140,100))
				dpg.add_theme_color(dpg.mvThemeCol_HeaderActive,(90,0,170,100))
		with dpg.theme() as searchBarTheme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing,0)
				dpg.add_theme_style(dpg.mvStyleVar_FramePadding,0,0)
				dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0)
		dpg.bind_item_theme(self.typeSelector, typeSelectorTheme)
		dpg.bind_item_theme(self.searchBar, searchBarTheme)
		dpg.bind_item_font(self.typeSelector, typeSelectorFont)
		dpg.bind_item_font(self.searchBar, searchBarFont)

Heimdall = SearchGUI()

