# A felhasználónak kérjetek be egy számot, és írjátok ki a kétszeresét
# Ezt egészen addig ismételjük, amíg a felhasználó nullát nem ír be


# DRY - don't repeat yourself

#number = int(input("Add meg a számot!"))
number = 100
while number != 0:
    number = int(input("Add meg a számot!"))
    print(number * 2)
