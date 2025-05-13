#TODO atividade
#NOTE: o usuário poderá cadastrar quantas pessoas quiser.
#NOTE: o programa deverá ter um menu com as opções: Cadastrar, listar, alterar, excluir e sair do programa.

'''
Crie um CRUD, ou seja, um programa que:
-Cadastre
-Lista
-Altere
-Exclua

O programa deverá cadastrar pessoas com os seguintes dados
Nome, CPF, E-mail, Telefone, Data de Nascimento, Gênero

'''

import os

pessoas = []

while True:

    print("Menu:")
    print("Cadastrar")
    print("Alterar")
    print("Excluir")
    print("Exibir")
    print("Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case 'Cadastrar':
            pessoa = {}
            pessoa['nome'] = input('Informe o nome: ')
            pessoa['email'] = input('Informe o email: ')
            pessoa['cpf'] = input('Informe o cpf: ')
            pessoa['telefone'] = input('Informe o telefone: ')
            pessoa['Data_de_nascimento'] = input('Informe a Data de nascimento: ')
            pessoa['Gênero'] = input('Informe o Gênero: ')

            pessoas.append(pessoa)
            os.system('cls')
            print(f'Pessoa cadastrada com sucesso!')
            for pessoa in pessoas:
                print(f"\n{'-'*20}\n")
            for chave in pessoa:
                        print(f"{chave.title()}: {pessoa.get(chave)}.")

        
        case 'Exibir':
            if not pessoa:
                 print("Nenhuma pessoa cadastrada.")
            else:
                for pessoa in pessoas:
                    print(f"\nPessoa")
                    print(f"{'-'*20}")
                for chave in pessoa:
                    print(f"{chave.title()}: {pessoa.get(chave)}")
        case 'Alterar':
            if not pessoas:
                print("Nenhuma pessoa cadastrada.")
            else:
                try:
                    indice = input("Digite o nome da pessoa que deseja alterar: ")
                    for chave in pessoa:
                        novo_valor = input(f"{chave.title()} atual: {pessoa[chave]} | Novo valor (pressione Enter para manter): ")
                        if novo_valor:
                            pessoa[chave] = novo_valor
                    print("Pessoa atualizada com sucesso!")
                except ValueError:
                    print("Por favor, digite um número válido.")
        case 'Excluir':
                try:
                    indice = input("Digite o nome da pessoa que deseja excluir: ")
                    confirmacao = input(f"Tem certeza que deseja excluir {pessoas}? (s/n): ")
                    if confirmacao.lower() == 's':
                        del pessoas[indice]
                        print("Pessoa excluída com sucesso!")
                    else:
                        print("Exclusão cancelada.")
                except ValueError:
                    print("Por favor, digite um número válido.")