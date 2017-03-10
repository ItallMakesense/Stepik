f = input()
if f == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a+b+c)/2
    print ((p*(p-a)*(p-b)*(p-c))**0.5)
elif f == 'прямоугольник':
    a, b = int(input()), int(input())
    print(a*b/1)
elif f == 'круг':
    r = int(input())
    print(3.14*r**2)
