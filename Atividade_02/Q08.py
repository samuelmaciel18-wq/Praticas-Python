maiores = 0

for i in range(5):
    idade = int(input(f"Qual a idade do estudante {i + 1}?: "))
    if idade >= 16:
        maiores += 1

print("Estudantes com mais de 15 anos:", maiores) 