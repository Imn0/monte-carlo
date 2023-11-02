from monte import Monte
from carlo import Carlo
import numpy as np
from pathlib import Path


def get_long_name(name, n_start, n_end, n_step, sets):
    return name + "_s" + str(n_start)+"_e"+str(n_end)+"_step"+str(n_step)+"_k"+str(sets)
    
class MonteCarlo:
    def __init__(self, start: np.single, stop: np.single, fun_to_integrate, true_value, 
                n_start=50, n_end=5000, n_step=50, sets=50, function_name="function", 
                threads=1, 
                min_val=None, max_val=None, eval_fun=None,
                save_graph=True, show_graph=False):
        Path("./results/" + function_name + "/").mkdir(parents=True, exist_ok=True)
        long_name = get_long_name(function_name, n_start, n_end, n_step, sets)
        print("Path created")
        print("Creating caluculator")
        carlo = Carlo(start, stop, fun_to_integrate,
                         n_start, n_end, n_step, sets, threads, min_val, max_val, eval_fun)
        print("creating grapher")
        monte = Monte(true_value, n_start, n_end, n_step, sets, function_name, long_name, save_graph, show_graph)
        
        print("calculating")
        monte(carlo())

        print("saving results")
        all_results = carlo.all_results
        avg_results = carlo.avg_results
        all_results.tofile(f'./results/{function_name}/all_{long_name}.csv', sep = ';')
        avg_results.tofile(f'./results/{function_name}/avg_{long_name}.csv', sep = ';')

