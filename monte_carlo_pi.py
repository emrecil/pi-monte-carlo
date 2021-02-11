import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from matplotlib import style

from estimate import estimate_pi

def add_patches(patches):
    """Adds patches to current plot"""
    for patch in patches:
        plt.gca().add_patch(patch)


def configure_plot(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def main(sample_size):
    style.use('fivethirtyeight')

    # plot of square, circle and random points
    plt.subplot(1, 2, 1)

    rect = Rectangle((0, 0), 1, 1, edgecolor='b', facecolor='none', linewidth=2)
    circle = Circle((0.5, 0.5), 0.5, edgecolor='r', facecolor='none', linewidth=2)
    add_patches([rect, circle])

    points = np.random.uniform(0, 1, (sample_size, 2))

    # Vector of pi values for each iteration
    pi_values = estimate_pi(points)

    # last estimated pi value
    pi_value = pi_values[-1]
    print("Estimated pi:", pi_value)

    # draws random points inside the square
    plt.scatter(points[:, 0], points[:, 1], c="green", marker="x", s=1/2)
    plt.axis('equal')
    title = 'Estimation of pi for n=' + str(sample_size) + ': pi=' + str(pi_value)
    configure_plot(title, 'x', 'y')

    # plot of pi value after each iteration
    plt.subplot(1, 2, 2)

    x = np.arange(0, len(pi_values))
    plt.plot(x, pi_values, '-', linewidth=1)

    title = 'Plot of estimated pi for each iteration'
    configure_plot(title, 'iteration', 'pi estimation')

    # horizontal line showing actual value of pi
    plt.hlines(np.pi, 0, x[-1], colors='red', linestyles='dashed', linewidth=1)

    plt.legend(('estimated pi', 'actual pi'))

    plt.show()


if __name__ == '__main__':
    sample_size = 10000

    if len(sys.argv) == 2:
        if str.isdigit(sys.argv[1]) and int(sys.argv[1]) > 0:
            sample_size = int(sys.argv[1])
        else:
            print("[Error] Argument must be a positive integer!")
            exit(-1)

    main(sample_size)
