# Kérj be egy egész számot és írd ki addig az összes egész páros számot!
# pl. 8, akkor legyen kiírva: 2, 4, 6, 8
# Pl. 3, akkor legyen kiírva: 2
# pl. 12, akkor legyen kiírva: 2, 4, 6, 8, 10, 12

limit = int(input("Adj meg egy számot"))
print(limit)
for i in range(2, limit + 1, 2):
    print(i)