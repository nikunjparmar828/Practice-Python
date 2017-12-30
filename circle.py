from math import pi

def area_circle(n):
    '''Without unittesting code was
    -------------------------------
    return pi*(n**2)
    -------------------------------
    '''
    if n<0:
        raise ValueError("Radius can not be nagative")#solved bug
    elif type(n) not in [int,float]:
        raise TypeError("Radiuse should be int or float")#solved bug
    else:
        return pi*(n**2)

