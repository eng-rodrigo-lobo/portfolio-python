'''
--------------- CALCULADORA --------------- 

Implementar um script que realize as 4 operações básicas, potência e raiz quadrada.

-------------------------------------------

'''
# Importando bibliotecas 
import os
import time

# Função para limpeza de tela do terminal
def limpar_tela():
    os.system('cls')

# Função de soma
def soma():
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    print("Calculando...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    resultado = num1 + num2
    print("{} + {} = {}".format(num1, num2, resultado))

# Função de subtração
def subtracao():
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    print("Calculando...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    resultado = num1 - num2
    print("{} - {} = {}".format(num1, num2, resultado))

# Função de multiplicação
def produto():
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    print("Calculando...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    resultado = num1 * num2
    print("{} x {} = {}".format(num1, num2, resultado))

# Função de divisão
def divisao():
    num1 = float(input("Insira o dividendo: "))
    num2 = float(input("Insira o divisor: "))
    print("Calculando...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    resultado = num1 / num2
    resto = num1 % num2
    print("{}/{} = {:.3f}, e o resto da divisão é {:.0f}".format(num1, num2, resultado, resto))

# Função de exponenciação
def potencia():
    num1 = float(input("Insira a base: "))
    num2 = float(input("Insira o expoente: "))
    print("Calculando...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    resultado = num1 ** num2
    print("{}^{} = {}".format(num1, num2, resultado))

# Função de radiciação (raiz quadrada apenas)
def raiz_quadrada():
    num1 = float(input("Insira o número: "))
    print("Calculando...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    resultado = num1 ** (0.5)
    print("Raiz quadrada de {} = {:.3f}".format(num1, resultado))

# Controla se o programa deve continuar no loop de funcionamento ou encerrar a operação 
calculadora_ON = True

while calculadora_ON:
    print("========== CALCULADORA ==========")
    print("0: SOMA")
    print("1: SUBTRAÇÃO")
    print("2: PRODUTO")
    print("3: DIVISÃO")
    print("4: POTÊNCIA")
    print("5: RAIZ QUADRADA")
    print("=================================")

    try:
        operacao = int(input("Selecione a operação desejada: "))

        if not 0 <= operacao <= 5:
            raise ValueError("Operação inválida. Por favor, digite um número entre 0 e 5.")
            
        # OPERAÇÃO SOMA
        if operacao == 0:
            soma()
        
        # OPERAÇÃO SUBTRAÇÃO
        if operacao == 1:
            subtracao()
        
        # OPERAÇÃO MULTIPLICACAO
        if operacao == 2:
            produto()
        
        # OPERAÇÃO DIVISAO
        if operacao == 3:
            divisao()
        
        # OPERAÇÃO EXPONENCIACAO
        if operacao == 4:
            potencia()
        
        # OPERAÇÃO RAIZ QUADRADA
        if operacao == 5:
            raiz_quadrada()
            
        print("=================================")
        reiniciar = int(input("Deseja realizar outra operação? [0] para SIM | [1] para NÃO\n"))
        if reiniciar == 0:
            print("Reiniciando calculadora")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            limpar_tela()
        elif reiniciar == 1:
            calculadora_ON = False

    except ValueError:
        print("\n-----------------------------------------------------------")
        print("Operação inválida. Por favor, digite um número entre 0 e 5.")
        print("Reiniciando a operação...")
        print("-----------------------------------------------------------\n")
        time.sleep(2)
        limpar_tela()

time.sleep(0.5)
print("--- Encerrando a calculadora ---")
