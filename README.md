# Monte Carlo 
Python program to calculate integral or area of a set. 

Example use 
```py
from montecarlo import MonteCarlo

def cbrt(x):
    return x*(1./3.)
MonteCarlo(0.0, 8, cbrt, function_name="cube_root")
```

For calculating are of a set you need to create function to determine if point is in or outside the set. 
```py
def pi_eval_fun(fun, point:(float, float)) -> int:
    if math.dist((0,0),point) <= 1.0:
        return 1
    return 0
```
Then you need to specify bounding box manually using ```min_val``` and ```max_val``` 
```py
MonteCarlo(-1.0, 1.0, None, true_value=math.pi, function_name="pi", threads=4, min_val=-1.0, max_val=1.0, eval_fun=pi_eval_fun)
```
