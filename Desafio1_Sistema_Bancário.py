menu = '''

[1] Depositrar
[2] Sacar
[3] Extrato
[0] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = int(input('Informe a opção: '))
    if opcao == 1:
        valor = float(input('Informe o valor do depósito: '))
        print(f'R${valor} depositado.')

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
        else:
            print('Operação falhou" o valor informado é inválido.')

    elif opcao == 2:
        valor = float(input('Informe o valor do saque: '))

        exceceu_saldo = valor > saldo
        exceceu_limite = valor > limite
        exceceu_saques = numero_saques >= LIMITE_SAQUES

        if exceceu_saldo:
            print(f'Operação falhou! Você não tem saldo suficiente. R${saldo}')

        elif exceceu_limite:
            print(f'Operação falhou! O valor do saque execede o limite de R${limite}.')
        
        elif exceceu_saques:
            print(f'Operação falhou! Número máximo de {numero_saques} saques excedido.')
    
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'Qauntidade de saques {numero_saques}/3')

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 3:
        print('\n======================== EXTRATO ========================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=========================================================')
    
    elif opcao == 0:
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')