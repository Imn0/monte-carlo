# całka od a do b
# f(x)
from random import uniform
import numpy as np
from multiprocessing import Process, Array

"""
 C/n *(b - a)M

    where C is the number of points in count of points that are counted as "inside the function", in code its count

    (b - a)M is area of the rectangle

    n is the number of points in current iteration
"""


class monte:

    """

    Monte is for calculation only



    """

    def __init__(self, start: float, stop: float, fun_to_integrate, n_start=50, n_end=5000, n_step=50, sets=50):
        self.a = start
        self.b = stop
        self.fun1 = fun(fun_to_integrate)
        self.min1, self.max1 = self.fun1.min_max(self.a, self.b)
        self.n_start = n_start
        self.n_end = n_end
        self.n_step = n_step
        self.n_count = (n_end - n_start)//n_step + 1
        self.sets = sets

    def _do_a_set(self, n) -> np.array:
        arr = np.empty(self.sets)
        for i in range(self.sets):
            arr[i] = self._do_a_one(n)
        return arr

    def _do_a_one(self, n) -> float:
        count = 0
        for i in range(n):
            x = uniform(self.a, self.b)
            y = uniform(self.min1, self.max1)
            val = self.fun1.function(x)

            if val >= 0:  # if function value is above X axis
                if y >= 0 and y <= val:  # when point is above 0 and below function we count it
                    count = count + 1
            else:  # if function value is below X axis
                if y <= 0 and y >= val:  # when point is below 0 and above function we count is a negative value
                    count = count - 1

        return count

    def _do_all(self) -> np.array:
        area = (self.max1 - self.min1) * (self.b - self.a)

        arr = np.empty(shape=(self.n_count, self.sets))
        count = 0
        for i in range(self.n_start, self.n_end + 1, self.n_step):
            arr[count] = self._do_a_set(i)/i  # here is the C/n step
            count = count + 1
            if count % 10 == 0:
                print(f"{count/self.n_count * 100: .0f}%")

        # here is *(b-a)M step, because are is the same for every iteration
        return arr*area

    def get_results(self):
        self.all_results = self._do_all()
        # self.all_results = self._split_work()
        return self.all_results

    def get_mean(self):
        self.avg_results = np.mean(self.all_results, axis=1)
        return self.avg_results


class fun:
    def __init__(self, function, eps=1000) -> None:
        self.function = function
        self.eps = eps

    def min_max(self, a: float,  b: float) -> tuple:
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


if __name__ == "__main__":

    print("whoops")
