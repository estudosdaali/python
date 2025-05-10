import os

pessoas = []

def exibir_pessoas():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    for i, pessoa in enumerate(pessoas):
        print(f"\nPessoa #{i}")
        print(f"{'-'*20}")
        for chave in pessoa:
            print(f"{chave.title()}: {pessoa.get(chave)}")

while True:
    print("\nMenu:")
    print("1 - Cadastrar nova pessoa")
    print("2 - Alterar pessoa existente")
    print("3 - Excluir pessoa")
    print("4 - Exibir pessoas cadastradas")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case '1':
            pessoa = {}
            pessoa['nome'] = input('Informe o nome: ')
            pessoa['email'] = input('Informe o email: ')
            pessoa['cpf'] = input('Informe o CPF: ')
            pessoa['telefone'] = input('Informe o telefone: ')
            pessoa['Data de nascimento'] = input('Informe a Data de nascimento: ')
            pessoa['Gênero'] = input('Informe o Gênero: ')

            pessoas.append(pessoa)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Pessoa cadastrada com sucesso!')
        case '2':
            exibir_pessoas()
            if pessoas:
                try:
                    indice = int(input("Digite o número da pessoa que deseja alterar: "))
                    if 0 <= indice < len(pessoas):
                        pessoa = pessoas[indice]
                        for chave in pessoa:
                            novo_valor = input(f"{chave.title()} atual: {pessoa[chave]} | Novo valor (pressione Enter para manter): ")
                            if novo_valor:
                                pessoa[chave] = novo_valor
                        print("Pessoa atualizada com sucesso!")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
        case '3':
            exibir_pessoas()
            if pessoas:
                try:
                    indice = int(input("Digite o número da pessoa que deseja excluir: "))
                    if 0 <= indice < len(pessoas):
                        confirmacao = input(f"Tem certeza que deseja excluir {pessoas[indice]['nome']}? (s/n): ")
                        if confirmacao.lower() == 's':
                            pessoas.pop(indice)
                            print("Pessoa excluída com sucesso!")
                        else:
                            print("Exclusão cancelada.")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
        case '4':
            exibir_pessoas()
        case '5':
            break
        case _:
            print("Opção inválida. Tente novamente.")
