import numpy as np
import matplotlib.pyplot as plt


class Automata:
    def __init__(self, dimensions=[], prob=0.1):
        if len(dimensions) != 2:
            raise TypeError('Container must be two dimensional.')
        self._dimensions = dimensions
        self._array = np.where(np.random.rand(dimensions[0],
                                              dimensions[1]) < prob,
                               1, 0)


    def run(self, iterations=1):
        pass


    def show(self):
        plt.matshow(self._array)
        plt.set_cmap('binary')
        plt.show()
