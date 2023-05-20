from matplotlib import pyplot as plt


def confusin_matrix_plot(matrix, conf_mx):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    cax = ax.matshow(matrix)
    fig.colorbar(cax)
    plt.matshow(conf_mx)
    plt.show()