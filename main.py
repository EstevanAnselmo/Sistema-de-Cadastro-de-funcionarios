def cadastrar_funcionario():
    nome = input("Qual é o seu nome?: ")
    idade = int(input("Qual é a sua idade?: "))
    setor = input("Qual é o seu setor?: ")
    cargo = input("Qual é o seu cargo?: ")

    # Exibindo dados
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Setor: {setor}")
    print(f"Cargo: {cargo}")

    # Verificando idade
    if idade <= 12:
        print(f"{nome}, você é uma criança.")
    elif idade < 18:
        print(f"{nome}, você é um adolescente.")
    elif idade < 60:
        print(f"{nome}, você é um adulto.")
    else:
        print(f"{nome}, você é um idoso.")

    # Verificando setor e cargo
    if setor == "TI":
        print("Você pertence ao setor de Tecnologia.")

        if cargo == "Assistente":
            print("Você é Assistente de TI.")
        elif cargo == "Analista":
            print("Você é Analista de TI.")
        else:
            print("Cargo não identificado.")

    elif setor == "RH":
        print("Você pertence ao setor de Recursos Humanos.")

        if cargo == "Assistente":
            print("Você é Assistente de RH.")
        elif cargo == "Analista":
            print("Você é Analista de RH.")
        else:
            print("Cargo não identificado.")

    else:
        print("Setor não identificado.")


# Sistema de cadastro
while True:
    print(
        """
==== SISTEMA DE CADASTRO ===

1 - Cadastrar funcionário
2 - Consultar funcionário
3 - Sair
"""
    )

    opcao = input("Escolha a opção: ")

    if opcao == "1":
        print("Cadastro selecionado.")
        cadastrar_funcionario()

    elif opcao == "2":
        print("Consulta selecionada.")

    elif opcao == "3":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")