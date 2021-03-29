
import numpy as np


def make_instance():
    # saber, archer, lancer, rider, caster, assassin, berserker, 
    # ruler, avenger, moon cancer, alter ego, foreigner, shielder
    type_matrix = np.array([[1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0], 
                            [2.0, 1.0, 0.5, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0], 
                            [0.5, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0],
                            [1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0], 
                            [1.0, 1.0, 1.0, 0.5, 1.0, 2.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0], 
                            [1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0], 
                            [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.5, 1.0], 
                            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0], 
                            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0], 
                            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 2.0, 1.0, 1.0, 1.0, 1.0], 
                            [0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0], 
                            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0], 
                            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])
    weak_matrix = np.where(type_matrix<2.0, 0.0, 1.0)
    resist_matrix = np.where(type_matrix<1.0, 1.0, 0.0)
    # type_matrix = type_matrix[0:13, 0:13]
    # set enemies
    # enemy1
    enemy1 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    # enemy2
    enemy2 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    # enemy3
    enemy3 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # combine enemy into one list
    enemies = np.array([enemy1, enemy2, enemy3])
    # set the number of party members
    num_party = 6
    # set feed_dict for hyperparameters
    feed_dict = {'h1': 10, 'h2': 10.0, 'h3': 10.0}
    return type_matrix, weak_matrix, resist_matrix, enemies, num_party, feed_dict