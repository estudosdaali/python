#importando a bibli
import os

#declaração da lista
nomes = ["Fulano","Ciclano","Ali","Beltrano","João","Maria","Papis"]

#tratamento de exceção
try:
    #loop infinito
    while True:
        #exibe a lista
        for i in range(len(nomes)):
            print (f"Nome de código {i}: {nomes[i]}.")
        #usuário deseja excluir
        opcao = input("Deseja excluir nome da lista? (s/n): ")
        match opcao:
            case "s":
                posicao = int(input("Informe o código do nome a ser alterado: "))
                del(nomes[posicao])
                os.system("cls")
                print("Item excluído com sucesso!\n")
                continue
            case "n":
                break
            case _:
                print("Opção Inválida.")
                continue
except Exception as e:
    print(f"Não foi possível deletar item da lista. {e}.")

