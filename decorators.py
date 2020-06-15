# importing libraries
import time
import logging
from datetime import datetime

# decorator to calculate duration
# taken by any function. 
def metrics_logger(func):
    def inner_wrap(*args, **kwargs):
        #Start time tracking
        time_start = datetime.now()
        print("{} process started: {}".format(func.__name__, str(time_start)))

        ret_func = func(*args, **kwargs)

        #End time tracking
        job_run_time = round((datetime.now() - time_start).total_seconds(), 3)
        print("{} process Completed: {}".format(func.__name__, str(time_start)))
        print("It took {} seconds for the process {} to complete".format(str(job_run_time), func.__name__))
        return ret_func
    return inner_wrap
