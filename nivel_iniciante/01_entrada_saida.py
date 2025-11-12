"""Exercício 1 - Entrada e Saída Simples

----------------------------------------
Leia dois números e mostre
- a soma
- a subtração
- a multiplicação
- a divisão entre eles
"""

# Entrada de dados, mas você pode já definir os valores da variável se quiser

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o primeiro número: "))

#O uso do float é para abranger uma maior quantidade de casos, não entraremos em questões quanto a exceções(erros)

#SOMA

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"""A soma de {num1} + {num2} é igual a {soma}
A subtração de {num1} - {num2} é igual a {subtracao}
A multiplicação de {num1} * {num2} é igual a {multiplicacao}
A divisão de {num1} / {num2} é igual a {divisao}
      """)