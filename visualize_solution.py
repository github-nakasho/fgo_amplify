
def visualize_solution(sol):
    # set types
    types = ['saber', 'archer', 'lancer', 'rider', 'caster', 'assassin', 'berserker', 
                'ruler', 'avenger', 'moon cancer', 'alter ego', 'foreigner', 'shielder']
    for i, j in enumerate(sol):
        for k, l in zip(j, types):
            if k == 1:
                print(str(i)+': '+l)
            