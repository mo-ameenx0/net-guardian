import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

import pkg_resources
from .dataset_reader import DatasetReader

@Gtk.Template(filename=pkg_resources.resource_filename(__name__, 'dataset_selection_page.glade'))
class DatasetSelectionPage(Gtk.Box):
    __gtype_name__ = 'DatasetSelectionPage'

    dialog_button = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    @Gtk.Template.Callback()
    def dialog_button_clicked_cb(self, *args, **kwargs):
        dialog = Gtk.FileChooserDialog(
            "Please choose a file", 
            self.get_toplevel(), 
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, 
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, 
            Gtk.ResponseType.OK)
        )

        filter_text = Gtk.FileFilter()
        filter_text.set_name("Dataset file")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            filepath = dialog.get_filename()
            DatasetReader.load_dataset(filepath)
        elif response == Gtk.ResponseType.CANCEL:
            pass

        dialog.destroy()
