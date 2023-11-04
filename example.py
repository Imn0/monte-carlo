from montecarlo import MonteCarlo
import math
import numpy as np



def pi_eval_fun(fun, point:(float, float)) -> int:
    if math.dist((0,0),point) <= 1.0:
        return 1
    return 0

def fun(x):
    return 4*x*((1-x)**3)

def cbrt(x):
    return x*(1./3.)

MonteCarlo(0.0, 8, cbrt, true_value=12, function_name="cube_root", threads=4)
MonteCarlo(0.0, math.pi, math.sin, true_value=2, function_name="sin")
MonteCarlo(0.0, 1, fun, true_value=0.2, function_name="cubic_blend", threads=4)
MonteCarlo(-1.0, 1.0, None, true_value=math.pi, function_name="pi", threads=4, min_val=-1.0, max_val=1.0, eval_fun=pi_eval_fun)
