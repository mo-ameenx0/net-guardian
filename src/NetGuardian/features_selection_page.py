import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

from .dataset_reader import DatasetReader

import pkg_resources

@Gtk.Template(filename=pkg_resources.resource_filename(__name__, 'features_selection_page.glade'))
class FeaturesSelectionPage(Gtk.Box):
    __gtype_name__ = 'FeaturesSelectionPage'

    features_flowbox = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    def load_features(self):
        radio_button_group = None
        for feature in DatasetReader.get_dataset_features():
            feature_row, radio_button_group = self.create_feature_row(feature, radio_button_group)
            self.features_flowbox.add(feature_row)

        self.features_flowbox.show_all()

    def create_feature_row(self, feature_name, radio_button_group):
        flowboxchild = Gtk.FlowBoxChild()

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        small_box = Gtk.Box()

        feature_label = Gtk.Label(label=feature_name)
        feature_label.set_halign(Gtk.Align.START)

        feature_check_button = Gtk.CheckButton()
        feature_check_button.set_active(True)

        small_box.pack_start(feature_check_button, False, False, 5)
        small_box.pack_start(feature_label, False, False, 5)

        label_radio_button = Gtk.RadioButton.new_with_label_from_widget(
            radio_button_group,
            label='Is label?'
        )

        main_box.pack_start(small_box, False, False, 5)
        main_box.pack_start(label_radio_button, False, False, 5)
        main_box.pack_start(Gtk.Separator(), False, False, 5)

        flowboxchild.add(main_box)

        return flowboxchild, label_radio_button