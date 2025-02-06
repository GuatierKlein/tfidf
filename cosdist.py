import math 

def distance_cosinus(vect1 : list[int], vect2 : list[int]):
    if len(vect1) != len(vect2):
        raise Exception("Vectors need to be the same length")
    dotprod = dot_product(vect1, vect2)
    normA = norm(vect1)
    normB = norm(vect2)

    return dotprod / normA * normB


def dot_product(vect1 : list[int], vect2 : list[int]):
    if len(vect1) != len(vect2):
         raise Exception("Vectors need to be the same length")

    dotprod = 0
    for i in range(0, len(vect1)):
        dotprod += vect1[i] * vect2[i]

    return dotprod

def norm(vect : list[int]):
    dimsum = 0 
    for dim in vect:
        dimsum += dim ** 2

    return math.sqrt(dimsum)
