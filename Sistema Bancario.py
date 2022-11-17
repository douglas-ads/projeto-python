menu="""
---------- MENU ----------
    [d] Depositar
    [s] Sacar
    [e] Extrato

    [q] Sair
--------------------------
Selecione uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao.lower() == "d":
        while True:
            valor = float(input("Digite o valor do depósito: "))
            if valor <= 0:
                print("Valor informado inválido!")
            if valor > 0:
                saldo += valor
                print("Deposito efetuado com sucesso")
                break

    elif opcao.lower() == "s":
        if numero_saques < LIMITE_SAQUES:
            while True:
                valor = float(input("Digite o valor do saque: "))
                if (valor <= limite) and (valor <= saldo):
                    print("Saque realizado com sucesso")
                    saldo -= valor
                    numero_saques += 1
                    break
                elif (valor > limite):
                    print("Valor ultrapassa o limite diário")
                elif (valor > saldo):
                    print("Saldo insuficiente")
        else:
            print("Numero máximo de saques diarios atingido")

    elif opcao.lower() == "e":
        print(f"Saldo atual é de R$ {saldo:.2f}")
    elif opcao.lower() == "q":
        break

    else:
        print("Opção inválida")
