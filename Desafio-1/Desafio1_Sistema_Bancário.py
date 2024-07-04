def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = '0001'

    while True:
        print(menu())
        opcao = int(input('Informe a opção: '))
        if opcao == 1:
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    LIMITE_SAQUES=LIMITE_SAQUES,
                )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)
        
        elif opcao == 0:
            break
        
        else:
            print('\033[31mOperação inválida, por favor selecione novamente a operação desejada.\033[m')

def menu():
    menu = '''
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
    ======================================
    '''
    return menu

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'\033[32m+ Depósito: R${valor:.2f}\n\033[m'
        print(f'\033[32mR${valor} depositado.\033[m')
    else:
        print('\033[31mOperação falhou o valor informado é inválido.\033[m')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    exceceu_saldo = valor > saldo
    exceceu_limite = valor > limite
    exceceu_saques = numero_saques >= LIMITE_SAQUES

    if exceceu_saldo:
        print(f'\033[31mOperação falhou! Você não tem saldo suficiente. Valor em conta R${saldo}\033[m')

    elif exceceu_limite:
        print(f'\033[31mOperação falhou! O valor do saque execede o limite de R${limite}.\033[m')
        
    elif exceceu_saques:
        print(f'\033[31mOperação falhou! Número máximo de {numero_saques} saques excedido.\033[m')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'\033[31m- Saque: R$ {valor:.2f}\n\033[m'
        numero_saques += 1
        print(f'Quantidade de saques \033[33m{numero_saques}/3\033[m')

    else:
        print('\033[31mOperação falhou! O valor informado é inválido.\033[m')

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print('\n======================== EXTRATO ========================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('=========================================================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n\033[31m Já existe usuário com esse CPF! \033[m')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('\033[34m=== Usuário criado com sucesso! ===\033[m')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n\033[34m=== Conta criada com sucesso! ===\033[m')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n\033[31m Usuário não encontrado, fluxo de criação de conta encerrado! \033[m')
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(linha)
        print('=' * 100)

main()