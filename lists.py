names = ["Joe", "Jack, Jane"]

# végigiterálunk a names változó elemein
for name in names:
    print(name)

for i, name in enumerate(names):
    print(i)
    print(name)


counter = 10
for name in names:
    print(counter)
    print(name)
    counter += 2

#Írd ki az első három hónap nevét egymás alá
# # Írd ki, hogy "Az év egyik hónapja január." az első három hónappal
# # Hozz létre egy listát a 3, 7, 9, 13 számokkal

numbers = [3, 7, 9, 13]
for number in numbers:
    print(number)


months = ["január", "február", "március"]
for i in months:
    print(i)

for month in months:
    print(f"Az év egyik hónapja {month}. ")

numbers = [3, 7, 9, 13]
sum = 0
for number in numbers:
    sum += number
print(sum)

numbers = [3, 7, 9, 13]
sum = 0 # 0
number = 3
sum += number # 0 + 3 = 3
number = 7
sum += number # 3 + 7 = 10
number = 9
sum += number # 10 + 9 = 19
number = 13
sum += number # 19 + 13 = 32
print(sum)