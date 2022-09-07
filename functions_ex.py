# Írjátok meg a signum függvényt!
# Ha a szám kisebb mint 0, akkor -1-et ad vissza
# Ha 0, akkor 0-át ad vissza
# Ha nagyobb, mont 0, akkor 1-et ad vissza


def signum(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1

print(signum(30))


# Írjatok egy függvényt, ami vár egy egész számot és visszaadja annak abszolútértékét.

def abs(n):
    if n < 0:
        return -n
    else:
        return n

print(abs(10))
print(abs(-20))

# Struktúrált programozás: minden függvényben CSAK egy return utasítás lehet
def abs_structured(n):
    if n < 0:
        return -n
    else:
        return n

def abs_structured(n):
    if n < 0:
        result = -n
    else:
        result = n
    return result

# Írjatok egy függvényt am várja a téglalap a és b oldalát ls visszaadja a területét

def calculate_perimeter(a, b):
    return 2 * (a +b)
print(calculate_perimeter(4, 6))


# Írjatok egy függvényt, mely várja a téglalap a és b oldalát és visszaadja a kerületet
def max(a, b):
    if a > b:
        return a
    else:
        return b


def area(a, b):
    return a * b
print(area(10, 5))
print(area(3, 2))

# Írjatok egy függvényt amely vár két számot, és visszadja a kettő közül a nagyobbat

# Vár egy számot és visszaadja a páros szöveget, ellenkező esetben hogy páratlan

def get_típe(n):
    if n % 2 == 0:
        return "páros"
    else:
        return "páratlan"

def get_type_sructured(n):
    if n % 2 == 0:
        type = "páros"
    else:
        type = "páratlan"
    return type

# Ha a függvény boolean értéket ad vissza, akkor logikai függvény: True, vagy False

# Írj egy is_even nevű függvényt, mely a paraméteréről eldönteni, hogy páros-e 
# True-t adjon vissza, ha páros, False értéket adjon vissza, ha páratlan

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_even_simple(n):
    return n % 2 == 0

print(signum(30))


if is_even(5):
    print("Ez egy szép páros szám")
else: 
    print("Ez egy páratlan szám")
