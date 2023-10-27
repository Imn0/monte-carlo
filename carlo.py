from monte_multi_thread import monte
import math
import matplotlib.pyplot as plt
import numpy as np


def x_squared(x):
    return math.sin(x)


class carlo:
    """
    carlo is for drawing whatever marco calculates, 
    first create carlo object, 
    then calculate
    then save_show
    """

    def __init__(self, start: float, stop: float, fun_to_integrate, true_value=0.0, n_start=50, n_end=5000, n_step=50, sets=50, name="function", threads = 0):
        """
        name is whatever u want your graph to be named
        """

        self.fun_to_integrate = fun_to_integrate
        self.true_value = true_value
        self.n_start = n_start
        self.n_end = n_end
        self.n_step = n_step
        self.sets = sets
        self.n_count = (n_end - n_start)//n_step + 1
        self.mnt = monte(start, stop, fun_to_integrate,
                         n_start, n_end, n_step, sets, threads)
        self.name = self.get_graph_name(name)

    def calculate(self):
        self.all_results = self.mnt.get_results()
        self.avg_results = self.mnt.get_mean()

    def save_show_plot(self, save=True, show=False):
        """
        by deafault this function only saves graph to /graphs in current directory
        ajust 'save' and 'show' to do what u want
        """
        print("rendering plot")
        plt.axhline(y=self.true_value, color='#00ff00',
                    linestyle='-', linewidth=3)
        for i in range(self.n_count):
            plt.scatter(np.array((i*self.n_step+self.n_start,)*self.sets), self.all_results[i],
                        label=f'Row {i}', color="b")

        plt.scatter(np.arange(self.n_start, self.n_end+1,
                    self.n_step), self.avg_results, color="r")

        if save:
            figure = plt.gcf()  # get current figure
            figure.set_size_inches(32, 18)
            plt.savefig("graphs/"+self.name + ".png", dpi=300)

        if show:
            plt.show()

        fig = plt.figure()
        plt.figure().clear()

    def get_graph_name(self, name):
        return name + "_s" + str(self.n_start)+"_e"+str(self.n_end)+"_step"+str(self.n_step)+"_k"+str(self.sets)


if __name__ == "__main__":
    print("whoops")
