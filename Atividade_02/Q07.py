numero = int(input("Digite um número: "))
positivos = 0
nulos = 0

for i in range(6):
    if numero > 0:
        positivos += 1
    elif numero == 0:
        nulos += 1
    if i < 5:
        numero = int(input("Digite outro número: "))

print("Positivos:", positivos)
print("Nulos:", nulos)