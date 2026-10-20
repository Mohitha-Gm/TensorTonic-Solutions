import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    v=np.array(v)
    w=np.array(w)
    dot=np.dot(v,w)
    v_mag=np.linalg.norm(v)
    w_mag=np.linalg.norm(w)
    if(v_mag==0 or w_mag==0):
        return np.nan
    else:
        c=dot/(v_mag*w_mag)
        c=np.clip(c,-1,1)
        return np.arccos(c)