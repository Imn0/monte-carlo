from montecarlo import MonteCarlo
import math
import numpy as np



#carl = carlo(0.0, 2.0, lambda x: x*x, 2.66, name="x_cubed", n_start=5000, n_end=5000, n_step=50, sets=50 )
#carl.calculate()
#carl.save_show_plot(show=True)

MonteCarlo(0.0, 8, np.cbrt, true_value=4, function_name="cube_root", threads=8)

# carl_2 = Carlo(0.0, math.pi, math.sin, true_value=2, name="sin", threads=4)
# carl_2.calculate()
# carl_2.save_show_plot()


# def fun(x):
#     return 4*x*((1-x)**3)

#                 # lambdas dont work
# carl_3 = Carlo(0.0, 1, fun, true_value=0.2, name="cubic_blend", threads=8)
# carl_3.calculate()
# carl_3.save_show_plot()

# def pi_eval_fun(fun, point:(np.single, np.single)) -> int:
#     if math.dist((0,0),point) <= 1.0:
#         return 1
#     return 0

# carl_pi = Carlo(-1.0, 1.0, None, true_value=math.pi, name="pi", threads=8, min_val=-1.0, max_val=1.0, eval_fun=pi_eval_fun)
# carl_pi.calculate()
# carl_pi.save_show_plot()
