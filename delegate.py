"""
as the duty of implementor:
    1) prepare your code in initialize method.
    2) cleanup after your code in terminate method.
    3) replace entry point of your algorithm in native_process method
    4) you must return a 1D array which is your proposed sequence of nodes for traveling through and an integer as
       total path cost of proposed path (permutation).

    exp:
        input :
            np.array([
                [0, 5, 4, 10],
                [5, 0, 8, 5],
                [4, 8, 0, 3],
                [10, 5, 3, 0]
            ])

        output:
            ([0, 1, 3, 2] , 17)

    *** input of your code will be a 2D numpy array where each index represents edge connecting nodes i and j.
    *** if two nodes do not have a edge connecting them directly, corresponding index will be set to -1.
"""
#from .exact.dynamic_programming import solve_tsp_dynamic_programming
from hda_tsp import *
import numpy as np


def native_id():
    # return your project name, team name or some unique id
    return "HDA-TSP"


def initialize():
    # setup initialization code in here
    # this method is called only once at the beginning benchmark
    return


def terminate():
    # setup cleanup code in here
    # this method is called only once at the end of benchmark
    return


def convert_input(raw_input):
    # convert our input here
    return

def convert_output(native_output):
    # convert your output here
    return native_output

# data?
def native_process(data):
    # delete line below, replace it with your own code
    # your return type must be a tuple consisting of permutation and total distance

    num_cities = 10
    num_iterations = 1000
    num_dragonflies = 100
    
    # Apply HDA to the TSP problem
    permutation, total_distance = hybrid_dragonfly_algorithm(num_dragonflies, num_cities, num_iterations)

    # return standard data
    return permutation, total_distance

# data?
# Test
data = 0
print(native_process(data))