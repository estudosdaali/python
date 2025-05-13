import os

lista = []

try:
    while True:
        usuario = {}

        print(f'{'='*20} CRUD COBRA{'='*20}')
        print(f'O que deseja fazer?')
        print('0 - Sair')
        print('1 - Cadastrar nova pessoa')
        print('2 - Listar usuários cadastrados')
        print('3 - Alterar usuário')
        print('4 - Excluir usuário')

        opcao = input(f'Escolha uma opção: ')

        match opcao:
            case '0':
                print(f'Programa encerrado')
                break
            case '1':
                usuario['nome'] = input('Informe o nome: ')
                usuario['email'] = input('Informe o email: ')
                usuario['cpf'] = input('Informe o cpf: ')
                usuario['telefone'] = input('Informe o telefone: ')
                usuario['Data_de_nascimento'] = input('Informe a Data de nascimento: ')
                usuario['Gênero'] = input('Informe o Gênero: ')

                lista.append(usuario)
                os.system('cls')
                print(f'{usuario}  cadastrado com sucesso!')
                continue
            case '2':
                os.systemas ('cls')
                for i in range(len(lista)):
                    print(f"Posição': {i}")
                    for chave in usuario:
                        print(f"{chave.title()}: {usuario.get(chave)}")
                    print('\n')
                continue
            case '3':
                os.system('cls')
                posicao = int(input('Informe a posição do usuário que deseja alterar: '))
                if lista[posicao]:
                    for chave in lista[posicao]:
                        print(f"{chave.title()}: {lista[posicao].get(chave)}")
                    print('\n')
                    dado = input('Informe o dado que deseja alterar: ')
                    if lista[posicao][dado]:
                        lista[posicao][dado] = input(f'Informe o novo valor para {dado}: ')
                        os.system('cls')
                        print(f'{dado} alterado com sucesso!')
                    else:
                        print('Inválido.')
                else:
                    print('Posição inválida.')
                continue
            case '4':
                os.system('cls')
                posicao = int(input('Informe a posição do usuário que deseja excluir: '))
                if lista[posicao]:
                        del lista[posicao]
                        os.system('cls')
                        print(f'Usuário excluído com sucesso!')
                else:
                    print('Não foi possível deletar.')
                continue
            case _:
                print('Opção inválida.')
                continue
except Exception as e:
    print(f'Não foi possível cadastrar pessoa. {e}.')
                          
                          
