import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a=np.array(a)
    b=np.array(b)
    dott=np.dot(a,b)
    a_mag=np.linalg.norm(a)
    b_mag=np.linalg.norm(b)
    if(a_mag==0 or b_mag==0):
        return 0.0
    else:
        cosi=dott/(a_mag*b_mag)
        return float(cosi)