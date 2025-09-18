import numpy as np
from scipy.sparse import csr_matrix

# Se crea una matriz con muchos ceros
dense_matrix = np.array([
    [0, 0, 3],
    [4, 0, 0],
    [0, 0, 5]
])

# Convertimos a formato disperso
sparse_matrix = csr_matrix(dense_matrix)

print(sparse_matrix)
# Muestra de salida: 
#   (0, 2)    3
#   (1, 0)    4
#   (2, 2)    5

print(sparse_matrix.toarray())  # Volvemos a la matriz normal
