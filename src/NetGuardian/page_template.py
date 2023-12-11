import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

import pkg_resources

@Gtk.Template(filename=pkg_resources.resource_filename(__name__, 'page_template.glade'))
class PageTemplate(Gtk.ScrolledWindow):
    __gtype_name__ = 'PageTemplate'

    page_content = Gtk.Template.Child()

    page_title = Gtk.Template.Child()

    def __init__(self, page_title, page_content_widget):
        super().__init__()

        self.page_title.set_text(page_title)
        self.page_content.pack_start(page_content_widget, True, True, 0)
