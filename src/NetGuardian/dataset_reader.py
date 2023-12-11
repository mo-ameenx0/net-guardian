import pandas as pd

from sklearn.model_selection import train_test_split

from typing import List

class DatasetReader:
    _self = None

    dataset: pd.DataFrame = None
    selected_features: List[str] = None
    label_feature: str = None

    def __new__(cls, *args, **kwargs):
        if cls._self is None:
            cls._self = super(DatasetReader, cls).__new__(cls)
        return cls._self

    @staticmethod
    def load_dataset(dataset_path):
        DatasetReader.dataset = pd.read_csv(dataset_path)

    @staticmethod
    def get_dataset_features():
        return DatasetReader.dataset.columns.tolist()

    @staticmethod
    def set_selected_features_and_label(selected_features, label_feature):
        DatasetReader.selected_features = selected_features
        DatasetReader.label_feature = label_feature

    @staticmethod
    def dataset_split_train_test(test_percentage=0.2):
        X = DatasetReader.dataset[DatasetReader.selected_features]
        y = DatasetReader.dataset[DatasetReader.label_feature]

        X_train, X_test, y_train, y_test = train_test_split(
                                                    X, y,
                                                    test_size = test_percentage,
                                                    stratify=y)

        return X_train, X_test, y_train, y_test
