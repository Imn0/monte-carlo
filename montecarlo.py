from carlo import carlo
import math


carl = carlo(-3.0, 4.0, lambda x: x**3, 43.75, name="x_cubed")
carl.calculate()
carl.save_show_plot()


carl_1 = carlo(0.0, 8, lambda x: x ** (1/3), true_value=12, name="cube root")
carl_1.calculate()
carl_1.save_show_plot()

carl_2 = carlo(0.0, math.pi, math.sin, true_value=2, name="sin")
carl_2.calculate()
carl_2.save_show_plot()


carl_3 = carlo(0.0, 1, lambda x: 4*x*((1-x)**3), true_value=0.2, name="idk")
carl_3.calculate()
carl_3.save_show_plot()


carl_pi = carlo(-1.0, 1.0, lambda x:  math.sqrt(1-x*x),
                true_value=math.pi, name="pi")
carl_pi.calculate()
carl_pi.all_results = carl_pi.all_results * 2  # integration gives us half of pi
carl_pi.avg_results = carl_pi.avg_results * 2
carl_pi.save_show_plot()
