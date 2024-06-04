#Calculadora Python

# Adição
def adicionar(x, y):
    return x + y

# Subtração
def subtrair(x, y):
    return x - y

# Multiplicação
def multiplicar(x, y):
    return x * y

# Divisão
def dividir(x, y):
    if y == 0:
        return "Erro:Impossível Divisão por Zero."
    else:
        return x / y
    
# Menu de opções
def exibir_menu():
    print("Menu:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

# Looping principal
while True:
    # Exibir o menu
    exibir_menu()
    
    # Solicitar a escolha do usuário
    escolha = input("Escolha uma operação (1/2/3/4/5): ")

    # Validar a escolha do usuário
    if escolha in ('1', '2', '3', '4', '5'):
        # Encerrar o programa
        if escolha == '5':
            print("Obrigado por testar minha calculadora. Até mais!")
            break
        
        # Solicitar os números
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Entrada inválida. Apenas números Porfavor.")
            continue

        # Executar a operação escolhida e mostrar o resultado
        if escolha == '1':
            print("Resultado:", adicionar(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtrair(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif escolha == '4':
            print("Resultado:", dividir(num1, num2))
    else:
        print("Erro: Opção inválida. Escolha um número de 1 a 5.")