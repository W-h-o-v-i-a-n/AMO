def factorial(x):
    if x < 0:
        raise ValueError
    else:
        res = 1
        for i in list(range(x)):
            res = res*(i+1)
        return res


def alg1(a, b, c):
    return (a*c)**2 + (b*c)**3 + c**8


def alg2(b, z, d, w, f):
    from math import sin, cos

    if z == 0: return 'ZeroDivisonError. Check your input.'
    elif b/z > d: return sin(w*f)
    else: return cos(w*f)


def alg3(a, b):
    if a < b : return 'a-b < 0. Enable to calculate (a-b)!.\n' \
                       'Check your input.'
    else: return factorial(a) * b / factorial(a-b)
