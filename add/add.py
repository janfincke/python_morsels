def add(*args):
    return list(list(sum(j) for j in zip(*rows)) for rows in zip(*args))


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
result = add(matrix1, matrix2)
print(result)