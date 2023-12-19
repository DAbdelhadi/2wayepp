
## Verstraete Scheme Equation 34
## https://arxiv.org/pdf/quant-ph/0404111.pdf

from important_functions import hashing, entropy

def verstraete_34(p00, p01, p10, p11):
    podd = 2 * (p00 + p01) * (p10 + p11)
    normalization_1 = p00 + p01
    normalization_2 = p10 + p11
    p = [p00, p01, p10, p11]
    v1 = [p00 / normalization_1, p01 / normalization_1]
    v2 = [p10 / normalization_2, p11 / normalization_2]
    rate = hashing(p) + podd / 4 * (entropy(v1) + entropy(v2))
    return max(rate,0)