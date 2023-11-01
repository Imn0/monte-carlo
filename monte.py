import math
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def x_squared(x):
    return math.sin(x)


class Monte:
    def __init__(self, true_value, n_start, n_end, n_step, sets, name, save, show):

        self.true_value = true_value
        self.n_start = n_start
        self.n_end = n_end
        self.n_step = n_step
        self.sets = sets
        self.n_count = (n_end - n_start)//n_step + 1
        self.name = self.get_graph_name(name)
        self.save = save
        self.show = show

    def __call__(self, results : [np.array, np.array]):
        """
        by deafault this function only saves graph to /graphs in current directory
        """
        all_results = results[0]
        avg_results = results[1]
        Path("./graphs").mkdir(parents=True, exist_ok=True)

        print("rendering plot")
        plt.axhline(y=self.true_value, color='#00ff00',
                    linestyle='-', linewidth=3)
        for i in range(self.n_count):
            plt.scatter(np.array((i*self.n_step+self.n_start,)*self.sets), all_results[i],
                        label=f'Row {i}', color="b")

        plt.scatter(np.arange(self.n_start, self.n_end+1,
                    self.n_step), avg_results, color="r")

        if self.save:
            figure = plt.gcf()  # get current figure
            figure.set_size_inches(16, 9)
            plt.savefig("graphs/"+self.name + ".png", dpi=300)

        if self.show:
            plt.show()

        plt.figure().clear()

    def get_graph_name(self, name):
        return name + "_s" + str(self.n_start)+"_e"+str(self.n_end)+"_step"+str(self.n_step)+"_k"+str(self.sets)
    