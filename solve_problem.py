#!/usr/bin/env python3

from amplify import Solver
from amplify.client import FixstarsClient


def solve_problem(model):
    # set client and parameters
    client = FixstarsClient()
    client.token = "xxxxx"
    client.parameters.timeout = 9999
    # set solver
    solver = Solver(client)
    # get result
    result = solver.solve(model)
    # extract value of objective function and binary variables
    obj, values = result[0].energy, result[0].values
    # get values of constraints
    broken = model.check_constraints(values)
    return obj, values, broken
