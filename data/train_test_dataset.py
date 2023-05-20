

def train_test_dataset(X, y):
    '''

    :param X:
    :param y:
    :return:
    '''
    X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
    return X_train, X_test, y_train, y_test