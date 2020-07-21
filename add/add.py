def add(*args):
    return list(list(sum(j) for j in zip(*rows)) for rows in zip(*args))