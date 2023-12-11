import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

from .page_template import PageTemplate
from .constants import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .features_selection_page import FeaturesSelectionPage
from typing import Dict

import sys
import pkg_resources

@Gtk.Template(filename=pkg_resources.resource_filename(__name__, 'main_page.glade'))
class MainPage(Gtk.ScrolledWindow):
    __gtype_name__ = 'MainPage'

    main_stack = Gtk.Template.Child()

    next_button = Gtk.Template.Child()
    back_button = Gtk.Template.Child()
    exit_button = Gtk.Template.Child()

    def __init__(self, pages: Dict[str, Gtk.Widget]):
        super().__init__()

        self.pages = pages

        for page_title, page_widget in self.pages.items():
            self.main_stack.add_named(
                PageTemplate(page_title, page_widget),
                page_title
            )

    @Gtk.Template.Callback()
    def next_button_clicked_cb(self, *args, **kwargs):
        current_page = self.main_stack.get_visible_child_name()
        
        page_titles = list(self.pages.keys())

        curren_page_idx = page_titles.index(current_page)

        next_page = page_titles[curren_page_idx + 1] \
                        if curren_page_idx + 1 < len(page_titles) \
                            else current_page

        page_widget = self.pages.get(next_page)

        if next_page == FEATURES_SELECTION_PAGE:
            page_widget:FeaturesSelectionPage
            page_widget.load_features()

        elif next_page == MODEL_SELECTION_PAGE:
            pass

        elif next_page == LOADING_PAGE:
            pass

        elif next_page == RESULT_PAGE:
            pass

        self.main_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT)
        self.main_stack.set_visible_child_name(next_page)

    @Gtk.Template.Callback()
    def back_button_clicked_cb(self, *args, **kwargs):
        current_page = self.main_stack.get_visible_child_name()
        
        page_titles = list(self.pages.keys())

        curren_page_idx = page_titles.index(current_page)

        previous_page = page_titles[curren_page_idx - 1] \
                        if curren_page_idx - 1 >= 0 \
                            else current_page
        
        self.main_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_RIGHT)
        self.main_stack.set_visible_child_name(previous_page)
    
    @Gtk.Template.Callback()
    def exit_button_clicked_cb(self, *args, **kwargs):
        sys.exit()
