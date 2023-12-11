import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

from .page_template import PageTemplate
from .constants import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .features_selection_page import FeaturesSelectionPage
    from .model_selection_page import ModelSelectionPage
from typing import Dict

import asyncio
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

    def _get_next_page(self):
        current_page = self.main_stack.get_visible_child_name()
        
        page_titles = list(self.pages.keys())

        curren_page_idx = page_titles.index(current_page)

        next_page_title = page_titles[curren_page_idx + 1] \
                        if curren_page_idx + 1 < len(page_titles) \
                            else current_page

        next_page_widget = self.pages.get(next_page_title)

        return next_page_title, next_page_widget

    def _get_previous_page(self):
        current_page = self.main_stack.get_visible_child_name()
        
        page_titles = list(self.pages.keys())

        curren_page_idx = page_titles.index(current_page)

        previous_page_title = page_titles[curren_page_idx - 1] \
                        if curren_page_idx - 1 >= 0 \
                            else current_page

        previous_page_widget = self.pages.get(previous_page_title)

        return previous_page_title, previous_page_widget

    @Gtk.Template.Callback()
    def next_button_clicked_cb(self, *args, **kwargs):
        next_page_title, next_page_widget = self._get_next_page()
        current_page = self.pages.get(self.main_stack.get_visible_child_name())

        if next_page_title == FEATURES_SELECTION_PAGE:
            next_page_widget:FeaturesSelectionPage
            next_page_widget.load_features()

        elif next_page_title == MODEL_SELECTION_PAGE:
            current_page:FeaturesSelectionPage
            current_page.set_selected_features()

        elif next_page_title == LOADING_PAGE:
            current_page:ModelSelectionPage
            task = asyncio.create_task(current_page.run_selected_models())
            task.add_done_callback(self.show_models_results_cb)

        self.main_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT)
        self.main_stack.set_visible_child_name(next_page_title)

    def show_models_results_cb(self, task, *args, **kwargs):
        results = task.result()

        result_page = self.pages.get(RESULT_PAGE)

        result_page.set_results(results)

        self.main_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT)
        self.main_stack.set_visible_child_name(RESULT_PAGE)


    @Gtk.Template.Callback()
    def back_button_clicked_cb(self, *args, **kwargs):
        previous_page_title, previous_page_widget = self._get_previous_page()
        
        self.main_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_RIGHT)
        self.main_stack.set_visible_child_name(previous_page_title)

    
    @Gtk.Template.Callback()
    def exit_button_clicked_cb(self, *args, **kwargs):
        sys.exit()
