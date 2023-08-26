# Needs a redo

from src.temp.windows import set_transparent_color
from src.Logger import Logger
import dearpygui.dearpygui as dpg
from screeninfo import get_monitors

class LoadingUI:
	"""
	 LoadingUI for Heimdall
	"""
	def __init__(self,debug) -> None:
		"""
		Setup for the Loading UI

		Args:
		  debug: Boolean, if True, the logger will print to the console.
		"""
		self.logger = Logger("Loading-UI",DEBUG=debug)
		self.initDPG()
		self.initDPGThemes()
		self.initMainWindow()
		self.start()

	def initDPG(self):
		"""
		It creates a viewport with the dimensions of the image, and sets the image as the background.
		"""
		dpg.create_context()
		with dpg.texture_registry():
			self.width, self.height, _, data = dpg.load_image("./src/gui/assets/textures/loader/logo.png")
			self.Image = dpg.add_dynamic_texture(self.width, self.height, data,tag="logo")
		dpg.create_viewport(
			title="Heimdall",              # Window Title (Also Application Title)
			large_icon="assets/icon.ico",  # "favicon" for Application
			small_icon="assets/icon.ico",  # "favicon" for Application
			always_on_top=True,
			decorated=False,               # Disables Windows Bar
			resizable=False,
			height=self.height,
			width=self.width,
			x_pos = -self.width,
			y_pos = -self.height,
			)
		dpg.setup_dearpygui()
		dpg.show_viewport()
		#Thanks to https://github.com/Atlamillias for this temporary workaround
		set_transparent_color((0,0,0))
		self.centerViewport()

	def centerViewport(self):
		"""
		It centers the window on the primary monitor
		"""
		for monitor in get_monitors():
			if monitor.is_primary:
				monitor_xd = monitor.width
				monitor_yd = monitor.height
		dpg.set_viewport_pos(pos=[
			(monitor_xd - self.width) / 2,
			(monitor_yd - self.height) / 2,
		])
		self.logger.debugMsg(f"""Window Size:
xd:{self.width}
yd:{self.height}
Window Position:
x:{(monitor_xd - self.width) / 2}
y:{(monitor_yd - self.height) / 2}
""")

	def initDPGThemes(self):
		"""
		We're creating a new theme, and then we're creating a new theme component that applies to all
		windows. Then we're adding a few styles to that component, and then we're binding the theme to the
		main window
		"""
		with dpg.theme() as mainWindowStyling:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
				dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0)
				dpg.add_theme_color(dpg.mvThemeCol_WindowBg,(0,0,0))
				dpg.bind_theme(mainWindowStyling)

	def initMainWindow(self):
		"""
		It creates a window with a tag of "mainWindow" and adds an image to it with a tag of "logo".
		"""
		# Main Window (Wrapper)
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
			dpg.add_image(texture_tag="logo",width=self.width,height=self.height)
		dpg.set_primary_window("mainWindow",True)

	def start(self):
		"""
		Starts the Loading UI
		"""
		dpg.start_dearpygui()

