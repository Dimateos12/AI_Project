import numpy as np


def is_five(label):
    return label == 5


def is_five_column_maker(y_train, y_test):
    # Przygotowanie nowej kolumny w danych treningowych
    train_labels_is_five = np.array([is_five(label) for label in y_train])

    # Przygotowanie nowej kolumny w danych testowych
    test_labels_is_five = np.array([is_five(label) for label in y_test])

