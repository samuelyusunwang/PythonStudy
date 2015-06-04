# Example for cProfile

import numpy as np
from numpy.linalg import eigvals

def run_experiment(nither=100):
    K = 100
    results = []
    for _ in range(nither):
        mat = np.random.randn(K, K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results

some_results = run_experiment()
print('Largest one we saw: %s' % np.max(some_results))

