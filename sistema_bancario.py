menu = """ \n\nDigite o número da operação que desejar realizar: \n
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair \n\n"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito de R${valor:.2f}.\n"

        else:
            print("\n\nO valor informado é inválido!\n\n")

    elif opcao == "2":
        valor = float(input("Insira o valor do saque: "))

        if valor > limite:
            print("Operação não realizada! O valor de saque excedeu o limite.")
        
        elif valor > saldo:
             print("Operação não realizada! Você não tem saldo suficiente.")

        elif numero_saques > LIMITE_SAQUES:
            print("Operação não realizada! Número máximo de saques excedido.")

        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + f"Operação realizada com sucesso! Seu novo saldo é de R${saldo} reais. \n"
            numero_saques = numero_saques + 1

        else:
            print("\n\nO valor informado é inválido!\n\n")

    elif opcao == "3":
        print(f"\n Saldo: R${saldo: .2f}")

    elif opcao == "4":
        break

    else:
        print("Operação não realizada! Por favor, selecione novamente a operação desejada.")



