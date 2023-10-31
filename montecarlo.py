from carlo import carlo
import math
import numpy as np

# carl = carlo(-3.0, 4.0, lambda x: x**3, 43.75, name="x_cubed")
# carl.calculate()
# carl.save_show_plot()

# carl_1 = carlo(0.0, 8, lambda x: np.cbrt(x), true_value=12, name="cube_root", threads=8)
# carl_1.calculate()
# carl_1.save_show_plot()

# carl_2 = carlo(0.0, math.pi, math.sin, true_value=2, name="sin", threads=8)
# carl_2.calculate()
# carl_2.save_show_plot()


# carl_3 = carlo(0.0, 1, lambda x: 4*x*((1-x)**3), true_value=0.2, name="idk", threads=8)
# carl_3.calculate()
# carl_3.save_show_plot()

def pi_eval_fun(fun, point:(float, float)) -> int:
    if math.dist((0,0),point) <= 1.0:
        return 1
    return 0

carl_pi = carlo(-1.0, 1.0, None, true_value=math.pi, name="pi", threads=8, min_val=-1.0, max_val=1.0, eval_fun=pi_eval_fun)
carl_pi.calculate()
carl_pi.save_show_plot(show=True)
