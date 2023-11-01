import numpy as np
import platform

if platform.system() == 'Linux':
    from pathos.multiprocessing import ProcessingPool as Pool
from tqdm import tqdm

"""
    C/n *(b - a)M

    where C is the number of points in count of points that are counted as "inside the function", in code its count

    (b - a)M is area of the rectangle

    n is the number of points in current iteration
"""

class Fun:
    def __init__(self, function, eps=1000) -> None:
        self.function = function
        self.eps = eps

    def min_max(self, a: np.single,  b: np.single) -> tuple:
        """ method to get minimal and maximal value of the function in given interval
        :param a: start of the interval
        :param b: end of the interval
        """
        n = int(abs(b - a)*self.eps)
        min_val = self.function(a)
        max_val = self.function(b)
        for i in range(n):
            cur = self.function(a + i / self.eps)
            if cur < min_val:
                min_val = cur
            if cur > max_val:
                max_val = cur

        return (min_val, max_val)
    
def deafault_eval_fun(fun: Fun, point: (np.single, np.single)) -> int:
        val = fun.function(point[0])
        if val >= 0:  # if function value is above X axis
            if point[1] >= 0 and point[1] <= val:  # when point is above 0 and below function we count it
                return 1
        else:  # if function value is below X axis
            if point[1] <= 0 and point[1] >= val:  # when point is below 0 and above function we count is a negative value
                return - 1
        return 0

class Monte:

    """
    Monte is for calculation only
    """

    def __init__(self, start: np.single, stop: np.single, fun_to_integrate, n_start=50, n_end=5000, n_step=50, sets=50, 
                threads=0, 
                min_val = None, max_val = None, eval = None):
        
        if threads < 1: 
            print("well now we gonna sit like this")
            while True:
                pass
            
        self.threads = threads

        self.a = start
        self.b = stop
        self.fun = Fun(fun_to_integrate)

        if min_val == None and max_val == None:
            self.min, self.max = self.fun.min_max(self.a, self.b)
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

    def _do_one_set(self, n: int, count: int) -> np.array:
        a = self.a
        b = self.b
        min_val = self.min
        max_val = self.max

        eval_function = self.eval_function
        fun = self.fun
        def _do_one_n(_) -> int:
            count = 0
            rng = np.random.default_rng()
            for _ in range(n):
                x = (b - a) * rng.random(dtype=np.single) + a
                y = (max_val - min_val) * rng.random(dtype=np.single) + min_val
                count += eval_function(fun,(x,y))
            return count
        
        if platform.system() == 'Linux':
            with Pool(self.threads) as p:
                r = list(tqdm(p.imap(_do_one_n, range(self.sets)), total=self.sets, desc=f"{count}/{self.n_count}"))
                return np.array(r)
        else:
            arr = np.empty(self.sets)
            for k in tqdm(range(self.sets),total=self.sets, desc=f"{count}/{self.n_count}" ):
                arr[k] = _do_one_n(k)
            return arr
        
    def _do_all(self) -> np.array:
        area = (self.max - self.min) * (self.b - self.a)

        arr = np.empty(shape=(self.n_count, self.sets))
        count = 0
        print(len(arr))
        for i in range(self.n_start, self.n_end + 1, self.n_step):
            arr[count] = self._do_one_set(i, count)/i  # here is the C/n step
            count = count + 1

        # here is *(b-a)M step, because are is the same for every iteration
        return arr*area

    def get_results(self):
        self.all_results = self._do_all()
        return self.all_results

    def get_mean(self):
        self.avg_results = np.mean(self.all_results, axis=1)
        return self.avg_results
