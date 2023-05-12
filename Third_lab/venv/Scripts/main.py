import math
import cmath
from typing import Optional, List
from fastapi import FastAPI, Query
from pydantic import BaseModel
from collections import Counter


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Complex(BaseModel):
    par_a: int
    par_b: int
    par_c: int
    par_complex: bool

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return

@app.get("/")
def root():
    return{"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return{"item_id" : item_id}

@app.get("/first_func/{wha}")
def BoolToStr(wha: bool):
    txt = str(wha)
    return txt

@app.get("/second_func/{rev}")
def Reverse(rev: str):
    revT = rev[::-1]
    return revT

@app.post("/third_func/")
@app.get("/third_func/")
def SumPos(mas: List[int] = Query(None, description="List of integers to calculate the sum of positive values.")):
    sum_pos = 0
    if (not mas):
        return 0
    else:
        for el in mas:
            if el > 0:
                sum_pos += el
    return sum_pos

@app.get("/fourth_func/{size}")
def Tringle(size: int):
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

@app.get("/fifth_func/{words}")
def Count_Repeat(words: str):
    k = {}
    for i in words:
        if i in k:
            k[i] += 1
        else:
            k[i] = 1
            
    sum_keys = 0
    for key, value in k.items():
        if value > 1:
            sum_keys = sum_keys + 1
    return sum_keys

@app.get("/sixth_func/{text}")
def Camel(text: str):
    for i in text:
        if(i.isupper()):
            text = text.replace(i, f'-{i.lower()}')
    return text

@app.get("/seventh_func/{n}")
def Preobraz(n: str):
    k = ""
    c = Counter(n)
    for i in c:
        k = k + str(c[i]) + i
    return k

@app.post("/eighth_func/")
def Sort(a: List[int]):
    b = sorted([item for item in a if item%2 != 0])
    odd_int = 0
    for i in range(len(a)):
        if a[i] %2 != 0:
            a[i] = b[odd_int]
            odd_int += 1
    return a

@app.post("/complex_func/")
async def discriminant_v2(comp: Complex):
    a = comp.par_a
    b = comp.par_b
    c = comp.par_c
    complex = comp.par_complex

    d = b**2-4*a*c
    if complex:
        x1 = (-b + cmath.sqrt(d))/(2 * a)
        x2 = (-b - cmath.sqrt(d))/(2 * a)
        return "Complex roots of the equation: " + str(x1) + ' ' + str(x2)
    else:
        if d < 0:
            return ("There is no solution")
        elif d == 0:
            x = -b/2 * a
            return "The root of the equation: " + str(x)
        else:                
            x1 = (-b + math.sqrt(d))/(2 * a)
            x2 = (-b - math.sqrt(d))/(2 * a)
            return "Roots of the equation: " + str(x1) + ' ' + str(x2)