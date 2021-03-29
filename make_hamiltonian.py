#!/usr/bin/env python3

from amplify import BinaryPoly, gen_symbols, sum_poly
from amplify.constraint import equal_to, greater_equal, less_equal


def make_hamiltonian(type_matrix, weak_matrix, resist_matrix, enemies, num_party, feed_dict):
    # set the number of types
    N = len(type_matrix)
    # set the number of enemies
    M = len(enemies)
    # set hyperparameters
    lambda_1 = feed_dict['h1']
    lambda_2 = feed_dict['h2']
    lambda_3 = feed_dict['h3']
    # make variables
    x = gen_symbols(BinaryPoly, num_party, N)
    # set one-hot constraint for types
    h1 = [equal_to(sum_poly([x[i][j] for j in range(N)]), 1) for i in range(num_party)]
    # set weak constraint
    h2 = [less_equal(sum_poly(N, lambda j: sum_poly(num_party, lambda l: sum_poly(N, lambda k: enemies[i][j]*weak_matrix[j][k]*x[l][k]))), 2) for i in range(M)]
    # set resist constraint
    h3 = [greater_equal(sum_poly(N, lambda j: sum_poly(num_party, lambda l: sum_poly(N, lambda k: enemies[i][j]*resist_matrix[j][k]*x[l][k]))), 1) for i in range(M)]
    # compute the total of constraints
    const = lambda_1 * sum(h1) + lambda_2 * sum(h2) + lambda_3 * sum(h3)
    # set objective function
    obj = sum_poly(num_party, lambda i: sum_poly(N, lambda j: sum_poly(N, lambda k: sum_poly(M, lambda l: x[i][j]*type_matrix[j][k]*enemies[l][k]))))
    # compute model
    model = - obj + const
    return x, model
