print("=== Lanchonete Sabor da Escola ===")
print("01. - Coxinha - R$ 6,00")
print("02. - Pastel - R$ 8,00")
print("03. - Suco - R$ 5,00")
print("04. - Hamburguer - R$ 17,00")

nome = input("Digite seu nome: ").strip()
if nome == "":
    nome = "Cliente"

opcao = input("Escolha um produto (01 a 04): ").strip()

produtos = {
    "01": ("Coxinha", 6.00),
    "02": ("Pastel", 8.00),
    "03": ("Suco", 5.00),
    "04": ("Hamburguer", 17.00),
}

if opcao in produtos:
    produto, preco = produtos[opcao]
    print(f"\nPedido realizado para: {nome}")
    print(f"Produto: {produto}")
    print(f"Valor: R$ {preco:.2f}")
else:
    print("\nOpção inválida. Escolha um número de 01 a 04.")