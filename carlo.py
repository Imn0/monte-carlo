import numpy as np
import platform
if platform.system() == 'Linux':
    from multiprocessing import  Pool
from tqdm import tqdm
from functools import partial


def min_max(function, a: np.single,  b: np.single, eps) -> tuple:
    """ method to get minimal and maximal value of the function in given interval
    :param a: start of the interval
    :param b: end of the interval
    """
    n = int(abs(b - a)*eps)
    min_val = function(a)
    max_val = function(b)
    for i in range(n):
        cur = function(a + i / eps)
        if cur < min_val:
            min_val = cur
        if cur > max_val:
            max_val = cur

    return (min_val, max_val)
    
def deafault_eval_fun(fun, point: (np.single, np.single)) -> int:
        val = fun(point[0])
        if val >= 0:  # if function value is above X axis
            if point[1] >= 0 and point[1] <= val:  # when point is above 0 and below function we count it
                return 1
        else:  # if function value is below X axis
            if point[1] <= 0 and point[1] >= val:  # when point is below 0 and above function we count is a negative value
                return - 1
        return 0

class Carlo:
    """
    Carlo is for calculation only
    """
    def __init__(self, start: np.single, stop: np.single, fun_to_integrate, n_start: int, n_end: int, n_step: int, sets: int, 
                thread_count=1, 
                min_val = None, max_val = None, eval = None, eps = 1000):
        
        if thread_count < 1: 
            print("well now we gonna sit like this")
            while True:
                pass

        self.threads = thread_count
        self.n = 0
        self.a = start
        self.b = stop
        self.fun = fun_to_integrate

        if min_val == None and max_val == None:
            self.min, self.max = min_max(fun_to_integrate,self.a, self.b, eps)
        else:
            self.min = min_val
            self.max = max_val
        if eval == None:
            self.eval_function = deafault_eval_fun
        else:
            self.eval_function = eval
            
        self.n_start = n_start
        self.n_end = n_end
        self.n_step = n_step
        self.n_count = (n_end - n_start)//n_step + 1
        self.sets = sets

    def _do_for_one_n(self, n, _) -> int:
        count = 0
        rng = np.random.default_rng()
        for _ in range(n):
            x = (self.b - self.a) * rng.random(dtype=np.single) + self.a
            y = (self.max - self.min) * rng.random(dtype=np.single) + self.min
            count += self.eval_function(self.fun, (x,y))
        return count

    def _do_one_set(self, n: int, count: int) -> np.array:
        f = partial(self._do_for_one_n, n)
        if platform.system() == 'Linux':
            with Pool(self.threads) as p:
                r = list(tqdm(p.map(f, range(self.sets)), total=self.sets, desc=f"{count}/{self.n_count}"))
                return np.array(r)
        else:
            arr = np.empty(self.sets)
            for k in tqdm(range(self.sets),total=self.sets, desc=f"{count}/{self.n_count}" ):
                arr[k] = f(k)
            return arr
        
    def _do_all(self) -> np.array:
        area = np.float32((self.max - self.min) * (self.b - self.a))

        arr = np.empty(shape=(self.n_count, self.sets))
        count = 0
        for i in range(self.n_start, self.n_end + 1, self.n_step):
            arr[count] = self._do_one_set(i, count)/i  # here is the C/n step
            count = count + 1

        # here is *(b-a)M step, because are is the same for every iteration
        return arr*area

    def __call__(self):
        self.all_results = self._do_all()
        self.avg_results = np.mean(self.all_results, axis=1)
        return [self.all_results, self.avg_results]