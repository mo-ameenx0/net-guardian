import time

from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class ModelClient:
    _self = None

    def __new__(cls, *args, **kwargs):
        if cls._self is None:
            cls._self = super(ModelClient, cls).__new__(cls)
        return cls._self
    
    @staticmethod
    def model_logistic_regression():
        model = LogisticRegression(max_iter=10000)

        return model

    @staticmethod
    def model_k_nearest_neighbor():
        model = KNeighborsClassifier()

        return model

    @staticmethod
    def model_decision_tree():
        model = DecisionTreeClassifier()

        return model

    @staticmethod
    def model_random_forest():
        model = RandomForestClassifier()

        return model

    @staticmethod
    def model_gradient_boosting():
        model = GradientBoostingClassifier()

        return model

    @staticmethod
    def voting_classifier(models):
        model = VotingClassifier(
            estimators=models,
            voting='soft'
        )

        return model

    @staticmethod
    def fit_model(models, X_train, y_train):
        model = ModelClient.voting_classifier(models)

        model.fit(X_train, y_train)

        return model

    @staticmethod
    def get_result(model, X_test, y_test):
        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        return {
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1
        }
