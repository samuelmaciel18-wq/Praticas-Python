import builtins

print = builtins.print

print("=== Lanchonete Sabor da Escola ===")
print("01. - Coxinha - R$ 6,00")
print("02. - Pastel - R$ 8,00")
print("03. - Suco - R$ 5,00")
print("04. - Hamburguer - R$ 17,00")

nome = input("Digite seu nome: ")
opcao = int(input("Escolha um produto (01 a 04): "))
quantidade = int(input("Digite a quantidade: "))
mesa = input("Deseja receber na mesa? (sim/não; entrega na mesa tem taxa de 10%): ").strip().lower()

if opcao == 1:
    preco = 6.00
    produto = "Coxinha"
elif opcao == 2:
    preco = 8.00
    produto = "Pastel"
elif opcao == 3:
    preco = 5.00
    produto = "Suco"
elif opcao == 4:
    preco = 17.00
    produto = "Hamburguer"
else:
    print("Opção inválida. Por favor, escolha um valor de 01 a 04.")
    preco = 0
    produto = "Produto não identificado"

if preco > 0:
    total = preco * quantidade

    if mesa == "sim":
        total = total * 1.10
    elif mesa in ("nao", "não"):
        total = total
    else:
        print("Digite sim ou não para a entrega na mesa.")
        total = 0

    print("\n=== Resumo do Pedido ===")
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Total a pagar: R$ {total:.2f}")
    print(f"Cliente: {nome}")
    pagamento = input("Qual será o método de pagamento? ")
else:
    print("Digite um pedido válido.")