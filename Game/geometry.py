import math

def get_distance(vertexA, vertexB):
    return math.sqrt((vertexA[0] - vertexB[0])**2 + (vertexA[1] - vertexB[1])**2)

def get_direction_vector(vertexA, vertexB):
    return (vertexB[0] - vertexA[0],vertexB[1] - vertexA[1])

def normalize_vector(vector):
    sqrt_dec = math.sqrt((vector[0])**2 + (vector[1])**2)
    return (vector[0]/sqrt_dec,vector[1]/sqrt_dec)