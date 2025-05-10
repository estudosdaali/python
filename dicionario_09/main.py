import os

pessoas = []


try:
    while True:
        cadastrar = input(f'Deseja cadastrar nova pessoa? (s/n):')
        match cadastrar:
            case 's':
                pessoa = {}

                pessoa ['nome'] = input('Informe o nome: ')
                pessoa ['email'] = input('Informe o email: ')
                pessoa ['cpf'] = input('Informe o cpf: ')


                pessoas.append(pessoa)
                os.system('cls')
                print(f'Pessoa cadastrada com sucesso!')
                for pessoa in pessoas:
                    print(f"\n{'-'*20}\n")
                    for chave in pessoa:
                        print(f"{chave.title()}: {pessoa.get(chave)}.")
                    
                continue
            case 'n':
                break
            case _:
                print('Opção inválida.')
                continue
except Exception as e:
    print(f'Não foi possível cadastrar pessoa. {e}.')
