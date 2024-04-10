def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = 15
print(fibonacci(n))


def je_palindrom(slovo):
    return slovo == slovo[::-1]

slovo = input("")
print(je_palindrom(slovo))


def spocti_pismena(slovo):
    pocet_pismen = {}

    for pismeno in slovo:
        if pismeno in pocet_pismen:
            pocet_pismen[pismeno] = pocet_pismen[pismeno] + 1
        else:
            pocet_pismen[pismeno] = 1

    return pocet_pismen

slovo = input("Zadej slovo: ")
vysledky = spocti_pismena(slovo)
for pismeno, pocet in vysledky.items():
    print(f"{pismeno}: {pocet}")