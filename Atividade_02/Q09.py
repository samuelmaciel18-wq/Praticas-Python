quantidade_notas = 4
soma = 0

for i in range(quantidade_notas):
    numero = float(input(f"Digite a nota {i + 1}: "))
    soma += numero

media = soma / quantidade_notas

print("A média das notas é:", media)