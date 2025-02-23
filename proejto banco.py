from datetime import datetime
import pytz

menu = """
[1] Depositar [2] Sacar
[3] Extrato   [4] Sair
=> """

saldo = 0
limite = 700
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4
numero_transacoes = 0
Limite_trasacoes = 10
data_transacoes = {}  # dicionario para armazenar data e hora das transações

fuso_horario = pytz.timezone('America/Sao_Paulo') #Definindo o fuso horario

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            data_transacoes[numero_transacoes] = datetime.now(fuso_horario) #Adicionado o fuso horario
            numero_transacoes += 1
            print(f"Depósito de R$ {valor:.2f} realizado em {data_transacoes[numero_transacoes -1].strftime('%d/%m/%Y %H:%M:%S')}") #Imprime a data e hora do deposito.

        else:
            print("Erro de operação! Selecione a operação correta.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro de Operação! Sem saldo suficiente.")
        elif excedeu_limite:
            print("Erro de Operação! Valor maior que o limite.")
        elif excedeu_saques:
            print("ERRO DE OPERAÇÃO! Limite de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            data_transacoes[numero_transacoes] = datetime.now(fuso_horario) #Adicionado o fuso horario
            numero_transacoes += 1
            print(f"Saque de R$ {valor:.2f} realizado em {data_transacoes[numero_transacoes -1].strftime('%d/%m/%Y %H:%M:%S')}") #Imprime a data e hora do saque.
            

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for i, transacao in enumerate(extrato.splitlines("saque")):
                if i in data_transacoes:
                    print(f"{data_transacoes[i].strftime('%d/%m/%Y %H:%M:%S')} - {transacao}") #Adicionado o fuso horario
        print(f"\nSaldo: R$ {saldo:.2f}")

        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")