menu = '''

[d]Deposito
[s]Saque
[e]Extrato
[q]Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:

    opcao=(input(menu))

    ###DEPOSITO###

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é invalido.")

    ###SAQUE###

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

            
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operacão falhou! Você não tem saldo o suficiente")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saque:
             print("Operação falhou! Número máximo de saque excede o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informadop é invalido.")

            ###EXTRATO###

    elif opcao == "e":
        print("\n============EXTRATO=========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao =="q":
        break

    else:
        print("Operação invalida, por favor selecione uma das opcoes.")
