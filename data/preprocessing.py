from sklearn.datasets import fetch_openml

def load_dataset():
    '''
    
    :return:
    '''
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    mnist.keys()
