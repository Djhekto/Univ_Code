def oneSquare(n):
    left, right = 0, n
    while right > left + 1:
        middle = (left + right) // 2
        if middle * middle >= n:
            right = middle
        else:
            left = middle
    if right * right == n:
        return right
    return -1
def twoSquares(n):
    a = 1
    while a * a < n:
        x = oneSquare(n - a * a)
        if x:
            return tuple(sorted((a, x)))
        a += 1
    return -1
def threeSquares(n):
    a = 1
    while a * a < n:
        x = twoSquares(n - a * a)
        if x:
            return tuple(sorted((x[0], x[1], a)))
        a += 1
    return -1
def fourSquares(n):
    a = 1
    while a * a < n:
        x = threeSquares(n - a * a)
        if x:
            return tuple(sorted((x[0], x[1], x[2], a)))
        a += 1
    return -1

asd=int(input())
print(fourSquares(asd))

