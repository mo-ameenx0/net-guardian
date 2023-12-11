import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from .main_page import MainPage
from .dataset_selection_page import DatasetSelectionPage
from .features_selection_page import FeaturesSelectionPage
from .constants import *

class NetGuardian(Gtk.Application):
    def __init__(self):
        super().__init__()

        pages = {
            DATASET_SELECTION_PAGE: DatasetSelectionPage(),
            FEATURES_SELECTION_PAGE: FeaturesSelectionPage(),
            MODEL_SELECTION_PAGE: Gtk.Label(label='Model Selection Page'),
            LOADING_PAGE: Gtk.Label(label='Loading Page'),
            RESULT_PAGE: Gtk.Label(label='Result Page')
        }

        main_page = MainPage(pages)

        screen = Gdk.Screen.get_default()
        width, height = screen.get_width(), screen.get_height()
        window_width = int(width * 0.5)
        window_height = int(height * 0.5)
        
        self.window = Gtk.Window()
        self.window.set_default_size(window_width, window_height)
        self.window.set_position(Gtk.WindowPosition.CENTER)

        self.window.add(main_page)

    def do_activate(self):
        self.add_window(self.window)
        self.window.show_all()
