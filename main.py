#zmienne typu logicznego
x = True
y = False
print(x)
print(y)
print("----")
b = None # taki javowy null
print(b)

print(5 == 4)
print(5 == 5)
print(5 != 1)

print(5 > 5)
print(2 < 4)
print(5 <= 5)
print(45 >= 5)

#instrukcje warunkowe
print("-------------")
if 5 == 5:
    print("Prawda")
print("Koniec")

if False:
    print("Prawda")

print("---")
if True:
    print("Prawda")

if 15 > 10:
    print("Wieksze")
elif 15 < 10:
    print("Mniejsze")
else:
    print("Równe")