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

    def create_feature_row(self, feature, radio_button_group):
        flowboxchild = Gtk.FlowBoxChild()

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        small_box = Gtk.Box()

        feature_name = Gtk.Label(label=feature)
        feature_name.set_halign(Gtk.Align.START)

        label_radio_button = Gtk.RadioButton.new_with_label_from_widget(
            radio_button_group,
            label='Is label?'
        )
        label_radio_button.set_sensitive(False)

        feature_check_button = Gtk.CheckButton()
        feature_check_button.connect('toggled', self.feature_check_button_toggle_cb, label_radio_button)

        small_box.pack_start(feature_check_button, False, False, 5)
        small_box.pack_start(feature_name, False, False, 5)

        main_box.pack_start(small_box, False, False, 5)
        main_box.pack_start(label_radio_button, False, False, 5)
        main_box.pack_start(Gtk.Separator(), False, False, 5)

        flowboxchild.add(main_box)

        return flowboxchild, label_radio_button

    def feature_check_button_toggle_cb(self, feature_check_button, label_radio_button, *args, **kwargs):
        if feature_check_button.get_active():
            label_radio_button.set_sensitive(True)
            return

        label_radio_button.set_active(False)
        label_radio_button.set_sensitive(False)

    def set_selected_features(self):
        selected_features = []
        label_feature = None

        for flowboxchild in self.features_flowbox.get_children():
            main_box = flowboxchild.get_child()

            main_box_children = main_box.get_children()
            
            small_box = main_box_children[0]
            label_radio_button = main_box_children[1]

            small_box_children = small_box.get_children()

            feature_check_button = small_box_children[0]
            feature_name = small_box_children[1]

            if not feature_check_button.get_active():
                continue

            selected_features.append(feature_name.get_text())

            if label_radio_button.get_active():
                label_feature = feature_name.get_text()

        DatasetReader.set_selected_features_and_label(selected_features, label_feature)
