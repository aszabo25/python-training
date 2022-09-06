if True:
    print("Ez mindig lefut")

if False:
    print("Ez sosem fut le")

if 5 > 10:
    print("Vajon lefut-e")

n = 10
n % 2 == 0  # Páros
n % 2 == 1  # Páratlan

szam = int(input("Adj meg egy számot"))
maradek = szam % 2
if maradek == 0:
    print("Páratlan")