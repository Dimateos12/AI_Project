from sklearn.metrics import confusion_matrix


def donfusin_matrix(y_train_5, y_train_pred):
    '''

    :param y_train_5:
    :param y_train_pred:
    :return:
    '''
    confusion_matrix(y_train_5, y_train_pred)
