def calculadora(num1, num2, operacao):
    # Faz a operação escolhida
    if operacao == "soma":
        return num1 + num2
    elif operacao == "sub":
        return num1 - num2
    elif operacao == "mult":
        return num1 * num2
    elif operacao == "div":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Erro: Operação inválida!"

def main():
    print("Bem-vindo à Calculadora!")
    
    # Pede os números e a operação
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (soma, sub, mult, div): ").lower()

    # Mostra o resultado
    resultado = calculadora(num1, num2, operacao)
    print("O resultado da operação é:", resultado)

main()
