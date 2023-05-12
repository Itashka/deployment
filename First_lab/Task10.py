import math
from sys import argv

_, a, b, c = argv

a = int(a)
b = int(b)
c = int(c)

d = b**2-4*a*c
if d < 0:
    print ("Нет решения")
elif d == 0:
    x = -b/2*a
    print("Корень уравнения:", round(x))
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print ("Корни уравнения: ", round(x1, 3), round(x2, 3))