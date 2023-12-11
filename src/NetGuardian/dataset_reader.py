import pandas as pd

from sklearn.model_selection import train_test_split

class DatasetReader:
    _self = None

    dataset: pd.DataFrame = None

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
    def get_dataset_with_selected_features(features):
        return DatasetReader.dataset[features]

    @staticmethod
    def dataset_split_train_test(test_percentage=0.2):
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = test_percentage,
                                                    stratify=y)

        return X_train, X_test, y_train, y_test
