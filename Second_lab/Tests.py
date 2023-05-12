import os
import math
import cmath
from sys import argv

def BoolToStr(wha):
    """
    Конвертирует заданное булевое значение в строку.
    
    >>> BoolToStr(False)
    'False'
    
    >>> BoolToStr(True)
    'True'
    """
    txt = str(wha)
    return txt

def Reverse(rev):
    """
    Возвращает строку в обратном порядке.
    
    >>> Reverse("False")
    'eslaF'
    
    >>> Reverse("True")
    'eurT'
    """
    revT = rev[::-1]
    return revT

def SumPos(mas):
    """
    Возвращает сумму всех положительных значений.
    Если массив пустой, то сумма равна 0.
    
    >>> SumPos([1, -1, 2, -3, -4])
    3
    
    >>> SumPos([-1, 1, -2, 3, 4])
    8

    >>> SumPos([])
    0
    """
    sum_pos = 0
    if (len(mas) == 0):
        return 0
    else:
        for el in mas:
            if el > 0:
                sum_pos += el
    return sum_pos

def Tringle(size):
    """
    Выводит треугольник из символов *.
    Высота треугольника равна числу, которое вы введете.
    
    >>> Tringle(3)
    '        *  \n       * *  \n      * * *  \n'
    >>> Tringle(5)
    '        *  \\n       * *  \\n      * * *  \\n     * * * *  \\n    * * * * *  \\n'
    """
    tr_str = ''
    m = (2 * size) - 2
    for i in range(0, size):
        for j in range(0, m):
            tr_str += ' '
        m = m - 1 # уменьшение m после каждого прохода цикла
        for j in range(0, i + 1):
            # вывод пирамиды из звёздочек
            tr_str += '* ' 
        tr_str += ' \n'
    return tr_str

def CountRepeat(string):
    """
    Возвращает количество символов, которые встречаются в строке более одного раза.
    Регистр символов не учитывается.
    
    >>> CountRepeat('asdazxcqweds')
    3
    
    >>> CountRepeat('aaaaassssddbbzzzqqqeer')
    7
    """
    k = {}
    for i in string:
        if i in k:
            k[i] += 1
        else:
            k[i] = 1
            
    sum_keys = 0
    for key, value in k.items():
        if value > 1:
            sum_keys = sum_keys + 1
    return sum_keys

def Camel(text):
    """
    Преобразует вводимую строку в стиль kebab-case. 
    Возвращаемая строка должна содержать только символы в нижнем регистре. 
    
    >>> Camel('camelsHaveThreeHumps')
    'camels-have-three-humps'
    
    >>> Camel('HiAllImNewbie')
    '-hi-all-im-newbie'
    """
    for i in text:
        if(i.isupper()):
            text = text.replace(i, f'-{i.lower()}')
    return text

from collections import Counter
def Preobraz(n):
    """
    Преобразует число в другое по следующему принципу:
    
    >>> Preobraz(1)
    '11'
    
    >>> Preobraz(21)
    '1211'
    
    >>> Preobraz(222222222222)
    '122'
    """
    n = str(n)
    k = ""
    c = Counter(n)
    for i in c:
        k = k + str(c[i]) + i
    return k

def Sort(a):
    """
    Преобразует число в другое по следующему принципу:
    
    >>> Sort([7, 8, 1])
    [1, 8, 7]
    
    >>> Sort([5, 8, 6, 3, 4])
    [3, 8, 6, 5, 4]
    
    >>> Sort([0, -2, -1, -3, 5, 7, 11, -11])
    [0, -2, -11, -3, -1, 5, 7, 11]
    """
    b = sorted([item for item in a if item%2 != 0])
    odd_int = 0
    for i in range(len(a)):
        if a[i] %2 != 0:
            a[i] = b[odd_int]
            odd_int += 1
    return a

def write_to_file(text, out_path: str) -> str:
    """
    """
    text = str(text)
    dir_path = os.path.dirname(out_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(out_path, 'a') as file:
        file.write(text + '\n')

def discriminant(a, b, c):
    """
    """
    a = int(a)
    b = int(b)
    c = int(c)

    no = 'Нет решения'

    d = b**2-4*a*c
    if d < 0:
        return no

    elif d == 0:
        x = -b/2*a
        return round(x, 3)
    else:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        return round(x1, 3), round(x2, 3)

def discriminant_v2(a, b, c, complex: bool):
    """
    Функция, которая принимает четыре параметра (a, b, c, complex) и выводит результат решения квардратного уравнения.
    Если d < 0, то не будет решения. НО, при указании параметра complex как True, функция выведет комплексные корни.
    Если d = 0, то выводится один корень.

    >>> discriminant_v2(1, 1, 1, False)
    'Нет решения'

    >>> discriminant_v2(1, 1, 1, True)
    'Комплексные корни уравнения:  (-0.5+0.8660254037844386j) (-0.5-0.8660254037844386j)'

    >>> discriminant_v2(1, 1, -1, False)
    'Корни уравнения:  0.6180339887498949 -1.618033988749895'
    """
    d = b**2-4*a*c
    if complex:
        x1 = (-b + cmath.sqrt(d))/(2 * a)
        x2 = (-b - cmath.sqrt(d))/(2 * a)
        return "Корни уравнения: " + str(x1) + ' ' + str(x2)
    else:
        if d < 0:
            return ("Нет решения")
        elif d == 0:
            x = -b/2 * a
            return "Корень уравнения: " + str(x)
        else:                
            x1 = (-b + math.sqrt(d))/(2 * a)
            x2 = (-b - math.sqrt(d))/(2 * a)
            return "Корни уравнения: " + str(x1) + ' ' + str(x2)

import doctest
doctest.testmod()