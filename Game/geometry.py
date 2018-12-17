from numpy.ma import sqrt


def get_distance(vertexA, vertexB):
    x = (vertexA[0] - vertexB[0])**2
    y = (vertexA[1] - vertexB[1])**2
    return sqrt( x + y)

def get_direction_vector(vertexA, vertexB):
    return (vertexB[0] - vertexA[0],vertexB[1] - vertexA[1])

def normalize_vector(vector):
    sqrt_dec = sqrt((vector[0])**2 + (vector[1])**2)
    return (vector[0]/sqrt_dec,vector[1]/sqrt_dec)