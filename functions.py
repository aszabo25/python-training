# Függvény definíció
def print_hello_world():
    print("hello")
    print("world")

# Saját függvényből lehet saját függvényt hívni
def print_hello_world_five_times():
    for i in range(0, 5):
        print_hello_world()

# egy paraméteres függvény, paraméter = argument
# a paraméter nem más, mint egy változó
# függvény definíció
# függvény definícióban lévő paraméter, azaz itt a text-et úgy hívjuk, hogy 
# Formális paraméter
def print_hello(text):
    print(f"hello {text}")
    print(text)

# Beépített függvények: input(), print(), int(), str(), range()
fruits = ["meggy", "cseresznye", "körte"]

#len()
print(len(fruits))  # length - hossz

print(len("hello world")) # stirng hosszát adja vissza

# függvény: névvel ellátott utasítás

# DRY
#print("hello")
#print("world")

print_hello_world() # meghívom a függvényt, azaz végrehajtásra kerül a függvényben az utasítás

print_hello_world

print("-------")

print_hello_world_five_times()

print_hello("joe")
print_hello("jack") # hívás helye
#Híváskor az aktuális paraméter Értéke bemásolódik a formális paraméterbe