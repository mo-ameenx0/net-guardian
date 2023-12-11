import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Pango, Gdk

import pkg_resources

@Gtk.Template(filename=pkg_resources.resource_filename(__name__, 'result_page.glade'))
class ResultPage(Gtk.Box):
    __gtype_name__ = 'ResultPage'

    results_box = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    def set_results(self, results):
        for child in self.results_box.get_children():
            self.results_box.remove(child)

        for result_title, value in results.items():
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            result_title_label = Gtk.Label(label=result_title)
            result_title_label.modify_font(Pango.FontDescription("12"))

            value_label = Gtk.Label(label=value)
            value_label.modify_font(Pango.FontDescription("12"))

            box.pack_start(result_title_label, False, False, 5)
            box.pack_start(value_label, False, False, 5)

            self.results_box.add(box)

        self.results_box.show_all()

        