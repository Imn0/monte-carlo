# Monte Carlo 
Python program to calculate integral or area of a set using monte carlo method.

Example use 
```py
from montecarlo import MonteCarlo

def cbrt(x):
    return x*(1./3.)
MonteCarlo(0.0, 8, cbrt, function_name="cube_root")
```

For calculating are of a set you need to create function to determine if point is in or outside the set. 
Note that evaluation function must take function and a point and return an integer value.
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

By default program samples multiple amounts of points, for each number of points program can perform multiple simulations and then take average by default it's 50.

All parameters

| Parametr         | Default          | Description |
| ---------------- | ---------------- | ----------- |
| start            | ```-```          | begining of integration interval |
| stop             | ```-```          | end of integration interval |
| fun_to_integrate | ```-```          | function to integrate, lambdas do not work when using multiple threads |
| true_value       | ```None```       | true value of integral, used for graphing the results, by default average of all simulated values will be used |
| n_start          | ```50```         | minimal amount of points that will be simulated |
| n_end            | ```5000```       | maximal amount of points that will be simulated |
| n_step           | ```50```         | every n_step'th value of n will be simulated |
| sets             | ```50```         | number of repeated simulations for each n value |
| function_name    | ```"function"``` | name of function, will be used to create directory and name files |
| threads          | ```1```          | number of threads that will be used to simulate single n value |
| min_val          | ```None```       | minimal value of function in given interval, will be calculated by program by default |
| max_val          | ```None```       | maximal value of function in given interval, will be calculated by program by default |
| eval_fun         | ```None```       | function to evaluate each of the sampled points |
| save_graph       | ```True```       | wheter to save graph to file |
| show_graph       | ```False```      | wheter to show a graph |
| eps              | ```100000```     | value used to calculate ```min_val``` and ```max_val```, is not used when ```min_val``` and ```max_val``` are provided |
