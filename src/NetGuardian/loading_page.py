import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

import pkg_resources

@Gtk.Template(filename=pkg_resources.resource_filename(__name__, 'loading_page.glade'))
class LoadingPage(Gtk.Box):
    __gtype_name__ = 'LoadingPage'

    def __init__(self):
        super().__init__()
