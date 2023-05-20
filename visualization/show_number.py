import matplotlib as mpl
import matplotlib.pyplot as plt


def show_digit(X):
    some_digit = X[41]
    some_digit_image = some_digit.reshape(28, 28)
    plt.imshow(some_digit_image, cmap=mpl.cm.binary)
    plt.axis("off")

    plt.show()
