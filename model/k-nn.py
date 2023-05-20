from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd


def knn(X,y):
    rs = RandomizedSearchCV(KNeighborsClassifier(algorithm='auto'), {
        'weights': ['uniform', 'distance'],
        'n_neighbors': [3, 4, 5]
    }, cv=5, return_train_score=False, n_iter=2)

    rs.fit(X, y)

    print("Najlepsze parametry: ", rs.best_params_)
    print("Najlepszy wynik: ", rs.best_score_)

    return rs
