import math
import matplotlib.pyplot as plt
import numpy as np

def x_squared(x):
    return math.sin(x)


class Monte:
    def __init__(self, true_value, n_start, n_end, n_step, sets, short_name,long_name, save = True, show = False):

        self.true_value = true_value
        self.n_start = n_start
        self.n_end = n_end
        self.n_step = n_step
        self.sets = sets
        self.n_count = (n_end - n_start)//n_step + 1
        self.name = long_name
        self.short_name = short_name
        self.save = save
        self.show = show

    def __call__(self, results : [np.array, np.array]):
        """
        by deafault this function only saves graph to /graphs in current directory
        """
        all_results = results[0]
        avg_results = results[1]
        

        print("rendering plot")
        plt.axhline(y=self.true_value, color='#00ff00',
                    linestyle='-', linewidth=1)
        for i in range(self.n_count):
            plt.scatter(np.array((i*self.n_step+self.n_start,)*self.sets), all_results[i], color="#aaa", s =2)

        plt.scatter(np.arange(self.n_start, self.n_end+1,
                    self.n_step), avg_results, color="r", s=4, label ="average")
    
        plt.legend(loc = "upper right")
        plt.xlabel("n")
        plt.ylabel("values")

        if self.save:
            figure = plt.gcf()  # get current figure
            figure.set_size_inches(16, 9)
            plt.savefig("./results/"+ self.short_name + "/" +self.name + ".png", dpi=300)

        if self.show:
            plt.show()

        plt.figure().clear()

    