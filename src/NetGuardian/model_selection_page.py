import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

from .model_template import ModelTemplate
from .model_client import ModelClient
from .dataset_reader import DatasetReader

import asyncio
import inspect
import uuid
import pkg_resources

@Gtk.Template(filename=pkg_resources.resource_filename(__name__, 'model_selection_page.glade'))
class ModelSelectionPage(Gtk.Box):
    __gtype_name__ = 'ModelSelectionPage'

    models_box = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):
        models = [method for method in dir(ModelClient) if method.startswith('model')]

        for idx, model in enumerate(models):
            self.models_box.pack_start(
                ModelTemplate(idx + 1, models),
                False,
                False,
                0
            )

    async def run_selected_models(self):
        models = []

        for child in self.models_box.get_children():
            models_combo_box = child.get_children()[1]

            selected_model = models_combo_box.get_active_text()

            if selected_model is not None:
                model = getattr(ModelClient, selected_model)()
                models.append((str(uuid.uuid4()), model))

        X_train, X_test, y_train, y_test = await asyncio.to_thread(DatasetReader.dataset_split_train_test)

        model = await asyncio.to_thread(ModelClient.fit_model, models, X_train, y_train)
        results = await asyncio.to_thread(ModelClient.get_result, model, X_test, y_test)

        return results
