import numpy as np

from simplicial_complex import SimplicialComplex


print('BETTI NUMBERS\n')

'''
Compute the Betti numbers of the 3-ball triangulated by a single tetrahedron.
'''

obs1 = SimplicialComplex()

'''Learn how to represent simplicial complexes by boundary matrices'''

# Add vertices
obs1.add_boundary_matrix(0, np.array([
    [1,1,1,1]
]))

# Relate vertices (rows) to edges (columns)
obs1.add_boundary_matrix(1, np.array([
    [1,1,1,0,0,0],
    [1,0,0,1,1,0],
    [0,1,0,1,0,1],
    [0,0,1,0,1,1]
]))

# Relate edges (rows) to faces (columns)
obs1.add_boundary_matrix(2, np.array([
    [1,1,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [1,0,0,1],
    [0,1,0,1],
    [0,0,1,1]
]))

# Relate faces (rows) to solid interior (column)
obs1.add_boundary_matrix(3, np.array([
    [1],
    [1],
    [1],
    [1]
]))

# Expected: [1,0,0,0]
print(f'Obstacles: {obs1.get_betti_numbers()}')


print('\nEULER CHARACTERISTIC\n')

'''
Euler characteristic computations
'''

print(f'Obs: {obs1.euler_characteristic()}')