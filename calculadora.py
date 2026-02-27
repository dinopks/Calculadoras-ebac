#TAREFA CALCULADORA
def calculadora(): #esse começo e fim foi  um inferno, programa o codigo n rodava nem a pau, despois de pesquisar  rodou
    print('Olá tudo bom? Bem vindo a Calculadora do Dino!!')
    print('Que tal Calcularmos algo?\n Escolha uma das opções:')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair da Calculadora')
#aqui em diante me deu muito trabalho, tive que pesquisar  pra aplicar o codigo.
    while True:
        try:
            escolha = int(input('Digite uma das opões acima entre: '))

            if escolha == 5:
              print('obrigado por usar a calculadora do Dino, até mais!!')
              break

            if escolha in [1,2,3,4]:
              num1 = float(input('Escolha o primeiro número: '))
              num2 = float(input('Escolha o segundo número: '))

              if escolha == 1:
                print(f'O Resultado da soma de {num1} + {num2} = {num1 + num2}')
              elif escolha == 2:
                print(f'O Resultado da Subtração {num1} - {num2} = {num1 - num2}')
              elif escolha == 3:
                print(f'O Resultado da Multiplicação {num1} * {num2} = {num1 * num2}')
              elif escolha == 4:
                if num2 != 0: #aqui dava muito erro, depois de pesquisar ficou meio bobo
                    print(f'O Resultado da divisão de {num1} / {num2} = {num1 / num2}')
                else:
                    print('Erro, é impossível dividir por 0')
            else:
                print('Opção inválida! digite apenas entre as cinco opções')
        except ValueError: #aqui pecaram em não ensinar isso, o curso foi bem complexo forçando pesquisa interna e por conta própria, mas foi bom pra aprender.
            print('por favor, digite apenas números para cálculos')

calculadora ()