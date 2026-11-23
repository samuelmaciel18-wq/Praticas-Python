numero = int(input("Escolha um número de 1 a 8: "))
if numero < 1 or numero > 8:
    print("Número inválido. Por favor, escolha um número entre 1 e 8.")
print(f"{numero}² = {numero**2}")