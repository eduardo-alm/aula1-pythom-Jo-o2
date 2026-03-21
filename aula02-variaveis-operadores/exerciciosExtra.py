nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

nova_idade = idade + 10
print(f"Sua idade daqui a 10 anos será {nova_idade}")

#EXERCICIO 2
n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2


print(f"Resulrado soma: {soma}, Resultado subtracao: {subtracao}, Resultado multiplicacao: {multiplicacao}")

#EXERCICIO 3

salario = int(input("Digite o seu salario: "))

salario10 = salario * 0.1
salario20 = salario * 0.2

print(f"Resultado salario com aumento de 10%: {salario10}, Resultado salario com aumento de 20%: {salario20}")

#EXERCICIO4
ac = float(input("Digite a nota da sua AC:  "))
agh = float(input("Digite a nota da sua AGH: "))
at = float(input("Digite a nota da sua AT: "))

nota_final = ((ac * 3) + (agh * 2) + (at * 5)) / 10

if nota_final < 6:
    print("Reprovado")
else:
    print("Aprovado")

print(f"Sua media do trimestre sera: {nota_final}.")

#EXERCICIO5
nomeProduto = input("Digite o nome do produto: ")
preco = int(input("Digite o preco do produto: "))

preco5 = preco * 0.1
precodesc5 = preco - preco5

print(f"O preco com desconto sera: {precodesc5}")
