import os


#dicionário
dados = {
    'nome': 'Alice',
    'idade': 29,
    'CPF': '0758214458'
}
try:
    while True:
        os.system('cls') #limpa o terminal
        for chave in dados:
            print(f"{chave.title()}: {dados.get(chave)}")

        #usuário informe se deseja inserir uma nova chave
        prosseguir = input('Deseja inserir novos dados? s/n: ')

        match prosseguir:
            case 's':
                #usuário informa o nome da chave adicional que deseja cadastrar
                nova_chave = input('\nInforme o nome da nova chave: ')
                dados[nova_chave] = input(f'Informe o valor de {nova_chave}: ') 
                
                continue
            case 'n':
                break
            case _:
                print('Opção inválida.')
                continue


except Exception as e:
    print(f"Mão foi possível inserir a nova chave: {e}.")