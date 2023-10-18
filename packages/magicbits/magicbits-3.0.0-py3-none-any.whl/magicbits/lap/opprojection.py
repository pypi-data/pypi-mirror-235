import numpy as np
def oprojection(of_vec: list, on_vec: list) -> tuple:
    """
    Calculates the orthogonal projection of one vector onto another vector.
    """

    v1 = np.array(of_vec)
    v2 = np.array(on_vec)

    scal = np.dot(v2, v1) / np.dot(v2, v2)
    vec = scal * v2
    return round(scal, 10), np.around(vec, decimals=10)

print("Orthogonal Project of a Vector:", oprojection([4.0,4.0],[8.0,2.0]))
