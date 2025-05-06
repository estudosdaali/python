#bibiloteca
import os

#dicionário
dados = {
    'nome': 'Alice',
    'idade': 29,
    'CPF': '0758214458'
}

#exibe os dados do dicionário
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}")


#usuário insere nova chave (email)
dados['email'] = input("\nInforme seu email: ")


#limpa o terminal e exibe os dados atualizados
os.system('cls')
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}")