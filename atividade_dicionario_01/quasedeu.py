#TODO: Atividade
"""
Crie um programa que se incializa com um dicionário zerado, e o usuário adicona e insere os seguintes dados:
- Nome, Data de Nascimento, CPF, e-mail, Gênero, Telefone, Altura, Peso e Tipo Sanguíneo;
Ao final, o programa exibe os dados do usuário e informe seu IMC;
"""
#Note: o usuário deve informar o valor APENAS dessas chaves;

import os

#dicionário
dados = {
    'nome': '',
    'data_nascimento': '',
    'cpf': '',
    'email': '',
    'genero': '',
    'telefone': '',
    'altura': 0.0,
    'peso': 0.0,
    'tipo_sanguineo': ''
}


#usuário insere os dados
dados['nome'] = input("\nInforme seu nome: ")
dados['data_nascimento'] = input("\nInforme sua data de nascimento: ")
dados['cpf'] = input("\nInforme seu CPF: ")
dados['email'] = input("\nInforme seu email: ")
dados['genero'] = input("\nInforme seu genero: ")
dados['telefone'] = input("\nInforme seu telefone: ")
dados['altura'] = int(input("\nInforme sua altura (em cm sem ponto ou vírgulas): "))
dados['peso'] = int(input("\nInforme seu peso (apenas kilos, sem ponto ou vírgulas): "))
dados['tipo_sanguineo'] = input("\nInforme seu tipo sanguíneo: ")

#exibe os dados do dicionário
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}")

#calculo do IMC
# Passo 1: converte a altura de cm para m
altura = dados['altura'] / 100
# Passo 2: calcula o IMC
imc = ['peso'] / ['altura'] * ['altura']
#Passo 3: exibe o IMC
print(f"\nSeu IMC é: {dados[imc]}")