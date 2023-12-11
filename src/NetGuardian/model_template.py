import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

import pkg_resources

@Gtk.Template(filename=pkg_resources.resource_filename(__name__, 'model_template.glade'))
class ModelTemplate(Gtk.Box):
    __gtype_name__ = 'ModelTemplate'

    models_combo_box = Gtk.Template.Child()
    model_number = Gtk.Template.Child()

    def __init__(self, model_number, model_names):
        super().__init__()

        self.model_number.set_text(f'Model {model_number}:')

        for model_name in model_names:
            self.models_combo_box.append_text(model_name)
        