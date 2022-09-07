# Szimuláljuk a dobókockadobást! 1-6

from random import choice, randint, shuffle

# randint fgv nem build-in function
# randint függvény a standard libary része
number = randint(1, 6)
print(number)

numbers = [2, 4, 6, 8]
shuffle(numbers)
print(numbers)

cards = ["alsó", "felső", "király", "ász"]
card = choice(cards)
print(card)
