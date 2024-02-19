# As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia,
# e R$ 0,25 se forem compradas pelo menos doze.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

QuantidadeMaca = int(input("Quantidade de Maças: "))

if QuantidadeMaca < 12:
    ValorTotal = QuantidadeMaca * 0.30
    print ("A quantidade de Maças é: ", QuantidadeMaca)
    print("O Valor total a ser pago é: R$", ValorTotal)
else:
    ValorTotal = QuantidadeMaca * 0.25
    print("A quantidade de Maças é: ", QuantidadeMaca)
    print("O Valor total a ser pago é: R$", ValorTotal)