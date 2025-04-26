#importação de bibliotecas
import os

#declaração da lista
cidades = [
        "Brasília", "Brasília", "São Paulo", 
        "Rio de Janeiro", "Belo Horizonte", "Brasília",
        "Goinânia", "Goinânia", "Palmas"
        ]

#tratamento de exceção  
try:
    #loop infinito
    while True:
        os.system("cls")#limpa o terminal
        pesquisa = input("Informe o nome da cidade a ser pesquisada: ") #usuário informa valor a ser pesquisado
        
        #retorna quantidade de valores encontrados
        resultado = cidades.count(pesquisa) #conta quantas vezes o valor aparece na lista

        #mostra resultado na tela
        if resultado !=0:
            print(f"{pesquisa} foi encontrado {resultado} vezes na lista.")
        else:
            print(f"{pesquisa} não foi encontrado na lista.")   

            #pergunta se o usuário deseja realizar uma nova pesquisa
        continuar = input("Deseja continuar? (s/n): ")

        #verificar se o usuário deseja continuar
        match continuar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                break 

    ...
except Exception as e:
    print(f"Não foi possível realizar a busca. {e}.")
