# importando a biblioteca
import os

#declaração da lista
lista = []

# try:
#     ...
# except Exception as e:
#     print(f"Não foi possível inserir item na lista. {e}.")
# finally:
#     ...

#tratamento de exceção
try:
    #loop infinito
    while True:
        item = input("Informe o nome do item ou deixe em brano para encerrar): ") #inpu
        os.system("cls") #limpa o terminal

        #verifica se o item está vazio ou não
        if item != "":
            lista.append(item) #adiciona o item na lista
            print("Inserido na lista com sucesso!") #mensagem de confirmação
            continue #continua o loop
        else:
            break


#ordena a lista 
    lista.sort() #ordena a lista em ordem alfabética
        
except Exception as e:
    print(f"Não foi possível inserir item na lista. {e}.")
finally:
    print("Lista de itens:\n") #imprime a lista
    for item in lista: #loop para imprimir os itens da lista
        print(item)


