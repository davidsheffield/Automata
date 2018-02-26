import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

from automata import Automata


class Conway(Automata):
    def __init__(self, dimensions=[], prob=0.1):
        super().__init__(dimensions, prob)


    def update(self):
        old_array = self._array.copy()
        for i in range(old_array.shape[0]):
            iprev = i - 1
            if i + 1 == old_array.shape[0]:
                inext = 0
            else:
                inext = i + 1
            for j in range(old_array.shape[1]):
                jprev = j - 1
                if j + 1 == old_array.shape[1]:
                    jnext = 0
                else:
                    jnext = j + 1
                neighbors = (old_array[iprev][jprev]
                             + old_array[iprev][j]
                             + old_array[iprev][jnext]
                             + old_array[i][jprev]
                             + old_array[i][jnext]
                             + old_array[inext][jprev]
                             + old_array[inext][j]
                             + old_array[inext][jnext])
                if old_array[i][j] == 1:
                    if (neighbors < 2) or (neighbors > 3):
                        self._array[i][j] = 0
                elif old_array[i][j] == 0:
                    if neighbors == 3:
                        self._array[i][j] = 1


    def run(self, iterations=1):
        for iteration in range(iterations):
            self.update()



    def run_show(self, fps=12):
        interval = int(1000.0 / fps)
        fig = plt.figure()
        plot = plt.matshow(self._array, fignum=0)

        def init_func():
            return plot.set_data(self._array)


        def update_func(frame):
            self.update()
            return plot.set_data(self._array)

        anim = FuncAnimation(fig, update_func, init_func=init_func,
                             interval=interval)
        plt.set_cmap('binary')
        plt.show()
