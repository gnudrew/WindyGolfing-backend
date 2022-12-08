"""Replicate a situation from psi_app where parallel processes clones started from the same inputs and problematically generated idential 'random' sequence of choices from an array"""

import numpy as np
from multiprocessing import Process, Pool

a = np.arange(10)
def choose_from_a(N):
    choices = [np.random.choice(a,1)[0] for _ in range(N)]
    # print(choices)
    return choices

if __name__ == '__main__':
    # array to randomly choose from
    print(a)

    with Pool(5) as pool:
        res_pool = pool.map(choose_from_a, [10, 10])
        for res in res_pool:
            print(res)

    new = False
    if new:
        # New... Generator
        rng = np.random.default_rng()
        c = rng.choice(a)
        print("Generator:", c)