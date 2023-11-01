from monte import Monte
from carlo import Carlo
import numpy as np


class MonteCarlo:
    def __init__(self, start: np.single, stop: np.single, fun_to_integrate, true_value, 
                n_start=50, n_end=5000, n_step=50, sets=50, function_name="function", 
                threads=1, 
                min_val=None, max_val=None, eval_fun=None,
                save_graph=True, show_graph=False):

        carlo = Carlo(start, stop, fun_to_integrate,
                         n_start, n_end, n_step, sets, threads, min_val, max_val, eval_fun)

        monte = Monte(true_value, n_start, n_end, n_step, sets, function_name, save_graph, show_graph)
        
        monte(carlo())
