import numpy as np
def entropy(p):
    """
    Computes the entropy of a probability distribution

    Args:
        p: an array of probabilities that sum to 1

    Returns: the entropy of the distribution

    """
    # Make sure input is a numpy array
    p = np.array(p)
    # Make sure the distribution sums to 1
    assert np.isclose(p.sum(), 1.0)
    # Make sure all probabilities are non-negative
    assert np.all(np.isclose(p-abs(p),0))

    # Compute the entropy
    e = 0
    for pi in p:
        if not np.isclose(pi,0):
            e -= pi * np.log2(pi)
    return e


def hashing(p):
    return 1 - entropy(p)