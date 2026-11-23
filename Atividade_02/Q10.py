numero = int(input("Digite um número: "))
pares = 0

for i in range(6):
    if numero % 2 == 0:
        pares += 1

    if i < 5:
        numero = int(input("Digite outro número: "))

print("Quantidade de números pares:", pares)