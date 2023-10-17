import statistics
import time
from functools import wraps


def measure_execution_time(
        num_exec: int = 5,
        warmup: int = 0,
        median: bool = False,
        quantiles: int = 0,
):
    '''
    Decorator to measure the execution time of a function.
    
    Args:
        num_exec (int): Number of times to execute the function.
        warmup (int): Number of times to execute the function before measuring.
        quantiles (int): Number of quantiles to print.
        median (bool): Whether to print the median.
        
    '''

    def measure_execution_time_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed_time_lst = []
            for i in range(num_exec + warmup):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()

                if i >= warmup:
                    elapsed_time = end_time - start_time
                    elapsed_time_lst.append(elapsed_time)

            print(f"{num_exec} loops:")
            print(f"mean: {statistics.mean(elapsed_time_lst)} sec.")
            
            if median:
                print(f"median: {statistics.median(elapsed_time_lst)} sec.")
                
            if quantiles > 0:
                qs = statistics.quantiles(elapsed_time_lst, n=quantiles)
                print(f"quantiles: {qs} sec.")
                
            print(f"std : {statistics.stdev(elapsed_time_lst)} sec.")
            print(f"max : {max(elapsed_time_lst)} sec.")
            print(f"min : {min(elapsed_time_lst)} sec.")
            return result

        return wrapper

    return measure_execution_time_wrapper
