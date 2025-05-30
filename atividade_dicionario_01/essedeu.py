#TODO: Atividade
"""
Crie um programa que se incializa com um dicionário zerado, e o usuário adicona e insere os seguintes dados:
- Nome, Data de Nascimento, CPF, e-mail, Gênero, Telefone, Altura, Peso e Tipo Sanguíneo;
Ao final, o programa exibe os dados do usuário e informe seu IMC;
"""
#Note: o usuário deve informar o valor APENAS dessas chaves;
import os

# dicionário
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

# usuário insere os dados
dados['nome'] = input("\nInforme seu nome: ")
dados['data_nascimento'] = input("\nInforme sua data de nascimento: ")
dados['cpf'] = input("\nInforme seu CPF: ")
dados['email'] = input("\nInforme seu email: ")
dados['genero'] = input("\nInforme seu genero: ")
dados['telefone'] = input("\nInforme seu telefone: ")
dados['altura'] = float(input("\nInforme sua altura (em metros, exemplo 1.75): "))  # Agora a altura é float
dados['peso'] = float(input("\nInforme seu peso (apenas quilos, exemplo 70.5): "))  # Peso como float
dados['tipo_sanguineo'] = input("\nInforme seu tipo sanguíneo: ")

# exibe os dados do dicionário
print("\nDados inseridos:")
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}")

# cálculo do IMC
# Passo 1: calcula o IMC
imc = dados['peso'] / (dados['altura'] ** 2)

# Passo 2: exibe o IMC
print(f"\nSeu IMC é: {imc:.2f}")  # Exibe o IMC com 2 casas decimais

# Passo 3: classifica o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:    
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc < 39.9:  
    classificacao = "Obesidade"
elif imc >= 40:
    classificacao = "Obesidade grave"
else:
    classificacao = "Classificação inválida"

#Passo 4: exibe a classificação do IMC
print(f"Classificação do IMC: {classificacao}")