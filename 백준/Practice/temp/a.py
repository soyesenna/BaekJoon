def f(x, y, z):
    if (x > y):
        if (x > z):
            return x
        else:
            return z
    else:
        if (y > z):
            return y
        else:
            return z

print(f(2, 3, 4), f(4, 3, 2), f(3, 2, 4))
