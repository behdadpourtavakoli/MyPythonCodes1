cdef extern from "math.h":
    float sin(float x)

def cy_sin(float x):
    cdef float result
    result = sin(x)
    return result

def python_sin(float x):
    import math
    return math.sin(x)
