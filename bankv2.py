from datetime import datetime
import pytz
import textwrap

# Definir fuso horário
fuso_horario = pytz.timezone('America/Sao_Paulo')

# Função para exibir o menu
def menu():
    opcoes = """
    =============== MENU ===============
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo Usuário
    [0] Sair
    ==> """
    return input(textwrap.dedent(opcoes))

# Função de depósito
def depositar(saldo, valor, transacoes):
    if valor > 0:
        saldo += valor
        data = datetime.now(fuso_horario)
        transacoes.append((data, f"Depósito: R$ {valor:.2f}"))
        print(f"Depósito de R$ {valor:.2f} realizado em {data.strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("Erro de operação! Selecione a operação correta.")
    return saldo, transacoes

# Função de saque
def sacar(saldo, valor, limite, numero_saques, limite_saques, transacoes):
    if valor > saldo:
        print("Erro de Operação! Saldo insuficiente.")
    elif valor > limite:
        print("Erro de Operação! Valor maior que o limite.")
    elif numero_saques >= limite_saques:
        print("Erro de Operação! Limite de saques excedido.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        data = datetime.now(fuso_horario)
        transacoes.append((data, f"Saque: R$ {valor:.2f}"))
        print(f"Saque de R$ {valor:.2f} realizado em {data.strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, numero_saques, transacoes

# Função de extrato
def mostrar_extrato(saldo, transacoes):
    print("\n================ EXTRATO ================")
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for data, descricao in sorted(transacoes):
            print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {descricao}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

# Função para criar usuário
def criar_usuario(usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso ===")

# Função para filtrar usuário
def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

# Função para criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None

# Função para listar contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:     {conta['agencia']}
            C/C:         {conta['numero_conta']}
            Titular:     {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função principal
def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 4

    saldo = 0
    limite = 700
    numero_saques = 0
    usuarios = []
    contas = []
    transacoes = []

    numero_conta = 1

    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("Informe o valor de depósito: "))  # Corrigido
            saldo, transacoes = depositar(saldo, valor, transacoes)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, numero_saques, transacoes = sacar(saldo, valor, limite, numero_saques, LIMITE_SAQUES, transacoes)
        elif opcao == "3":
            mostrar_extrato(saldo, transacoes)
        elif opcao == "4":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            criar_usuario(usuarios)
        elif opcao == "0":
            print("Saindo do sistema. Obrigado por usar nossos serviços!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
