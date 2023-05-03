def rgb(r, g, b):
    def bound(x):
        if x < 0: return 0
        if x > 255: return 255
        return x
    r = bound(r)
    g = bound(g)
    b = bound(b)
    val = '%02x%02x%02x' % (r,g,b)
    return val.upper()