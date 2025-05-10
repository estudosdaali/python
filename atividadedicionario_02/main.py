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

try:
    while True:

        print("Menu:")
        print("Cadastrar")
        print("Alterar")
        print("Excluir")
        print("Exibir pessoas cadastradas")
        print("Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case 'Cadastrar':
                pessoa = {}

                pessoa['nome'] = input('Informe o nome: ')
                pessoa['email'] = input('Informe o email: ')
                pessoa['cpf'] = input('Informe o cpf: ')
                pessoa['telefone'] = input('Informe o telefone: ')
                pessoa['Data de nascimento'] = input('Informe a Data de nascimento: ')
                pessoa['Gênero'] = input('Informe o Gênero: ')

                pessoas.append(pessoa)
                os.system('cls')
                print(f'Pessoa cadastrada com sucesso!')
                for pessoa in pessoas:
                    print(f"\n{'-'*20}\n")
                    for chave in pessoa:
                        print(f"{chave.title()}: {pessoa.get(chave)}.")

        
            case 'Alterar':
                print('Quem você gostaria de alterar?')
              