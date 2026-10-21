def f(x, y):
    t = 0
    for i in x:
        t = t + i
    a = t / len(x)
    if a > y:
        return "Good job"
    else:
        return "Take more breaks"

def calc(m):
    s = m * 60
    return s

l = [5, 10, 15]
print(f(l, 10))
print(calc(5))
