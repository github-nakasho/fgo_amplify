#!/usr/bin/env python3

from amplify import decode_solution

import make_hamiltonian as mh
import make_instance as mi
import solve_problem as sp
import visualize_solution as vs


if __name__ == '__main__':
    # get instance information
    type_matrix, weak_matrix, resist_matrix, enemies, num_party, feed_dict = mi.make_instance()
    # set hamiltonian for model
    x, model = mh.make_hamiltonian(type_matrix=type_matrix, 
                                    weak_matrix=weak_matrix, 
                                    resist_matrix=resist_matrix, 
                                    enemies=enemies, 
                                    num_party=num_party, 
                                    feed_dict=feed_dict)
    # solve with amplify
    obj, values, broken = sp.solve_problem(model=model)
    # execute decoding
    x_sol = decode_solution(x, values)
    # visualize solution
    print('***** Enemies *****')
    vs.visualize_solution(sol=enemies)
    print('***** My party *****')
    vs.visualize_solution(sol=x_sol)    
    