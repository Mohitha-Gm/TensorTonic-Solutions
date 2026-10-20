import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    x=np.array(x)
    y=np.array(y)
    result=0
    for i in range(0,len(x)):
        result+=x[i]*y[i]
    return float(result)