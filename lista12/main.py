import os

nomes = ["Georgia", "Carolina", "Erenice","Birabella", "Marimel", "Jean Claude van Damme"]

try:
   for i in range(len(nomes)):
       print(f"Código {i}: {nomes[i]}.")
       posicao = int(input("Informe o código do item a ser separado: "))
       nome_separado = nomes.pop(posicao) # separao item da lista
       os.system("cls")
       print(nome_separado)
       print(nomes)
except Exception as e:
    print(f"Não foi possível separar item da lista. {e}.")