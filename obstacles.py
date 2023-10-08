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

# Solid Triangle "."

triangle = SimplicialComplex()

'''Learn how to represent simplicial complexes by boundary matrices'''

# Add vertices
triangle.add_boundary_matrix(0, np.array([
    [1,1,1]
]))

# Relate vertices (rows) to edges (columns)
triangle.add_boundary_matrix(1, np.array([
    [1,0,1],
    [1,1,0],
    [0,1,1]
]))

# Relate edges (rows) to faces (columns)
triangle.add_boundary_matrix(2, np.array([
    [1],
    [1],
    [1]
]))

# # Relate faces (rows) to solid interior (column)
# obs1.add_boundary_matrix(3, np.array([
#     [1],
#     [1],
#     [1],
#     [1]
# ]))

# Expected: [1,0,0,0]
print(f'Triangle: {triangle.get_betti_numbers()}')


# Empty Triangle "O"

etriangle = SimplicialComplex()

'''Learn how to represent simplicial complexes by boundary matrices'''

# Add vertices
etriangle.add_boundary_matrix(0, np.array([
    [1,1,1]
]))

# Relate vertices (rows) to edges (columns)
etriangle.add_boundary_matrix(1, np.array([
    [1,0,1],
    [1,1,0],
    [0,1,1]
]))

# Relate edges (rows) to faces (columns)
etriangle.add_boundary_matrix(2, np.array([
    [0],
    [0],
    [0]
]))

# # Relate faces (rows) to solid interior (column)
# obs1.add_boundary_matrix(3, np.array([
#     [1],
#     [1],
#     [1],
#     [1]
# ]))

# Quad B

quad  = SimplicialComplex()

'''Learn how to represent simplicial complexes by boundary matrices'''

# Add vertices
quad.add_boundary_matrix(0, np.array([
    [1,1,1,1]
]))

# Relate vertices (rows) to edges (columns)
quad.add_boundary_matrix(1, np.array([
    [1,0,1,1,0],
    [1,1,0,0,0],
    [0,1,1,0,1],
    [0,0,0,1,1]
]))

# Relate edges (rows) to faces (columns)
quad.add_boundary_matrix(2, np.array([
    [1,0],
    [1,0],
    [1,1],
    [0,1],
    [0,1]
]))

# Relate faces (rows) to solid interior (column)
quad.add_boundary_matrix(3, np.array([
     [0],
     [0]
 ]))


# Tetrahedron solid 

Tent  = SimplicialComplex()

'''Learn how to represent simplicial complexes by boundary matrices'''

# Add vertices
Tent.add_boundary_matrix(0, np.array([
    [1,1,1,1]
]))

# Relate vertices (rows) to edges (columns)
Tent.add_boundary_matrix(1, np.array([
    [1,0,1,1,0, 0],
    [1,1,0,0,0, 1],
    [0,1,1,0,1, 0],
    [0,0,0,1,1, 1]
]))

# Relate edges (rows) to faces (columns)
Tent.add_boundary_matrix(2, np.array([
    [1,0,1,0],
    [1,0,0,1],
    [1,1,0,0],
    [0,1,1,0],
    [0,1,0,1],
    [0,0,1,1]
]))

# Relate faces (rows) to solid interior (column)
Tent.add_boundary_matrix(3, np.array([
     [1],
     [1],
     [1],
     [1]
 ]))

print(f'Solid Triangle: {triangle.get_betti_numbers()}')
# Expected: [1,0,0]
print(f'Empty Triangle: {etriangle.get_betti_numbers()}')
# Expected: [1,1,0]
print(f'Quad: {quad.get_betti_numbers()}')
# Expected: [1,0,1,0]
# Gives: [1,0,-1,1]
print(f'Tent: {Tent.get_betti_numbers()}')
# Expected: [1,0,1,0]
# Gives: [1,0,-1,1]


print('\nEULER CHARACTERISTIC\n')

'''
Euler characteristic computations
'''

print(f'Solid Triangle: {triangle.euler_characteristic()}')
print(f'Empty Triangle: {etriangle.euler_characteristic()}')
print(f'Quad: {quad.euler_characteristic()}')
print(f'Tent: {Tent.euler_characteristic()}')