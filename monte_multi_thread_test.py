import matplotlib.pyplot as plt
import numpy as np
from monte_multi_thread import monte

if __name__ == "__main__":
    n_start = 50
    n_end = 5000
    n_step = 50
    n_count = 100
    sets = 50
    mnt = monte(-3.0, 4.0, lambda x: x**3)
    all_results = mnt.get_results()
    avg_results = mnt.get_mean()
    print("rendering plot")
    plt.axhline(y=43.75, color='#00ff00',
                linestyle='-', linewidth=3)
    for i in range(n_count):  # n_count
        plt.scatter(np.array((i*n_step+n_start,)*sets), all_results[i],
                    label=f'Row {i}', color="b")

        plt.scatter(np.arange(n_start, n_end+1,
                    n_step), avg_results, color="r")

    figure = plt.gcf()  # get current figure
    figure.set_size_inches(32, 18)
    plt.savefig("graphs/" + "hhh.png", dpi=300)

    fig = plt.figure()
    plt.figure().clear()
