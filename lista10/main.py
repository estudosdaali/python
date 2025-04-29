#Aqui tem JOIN. Join é um comando que pega os valores de duas o mais listas e junta em uma única variável


#declarando a lista
dias = [
        "Domingo",
        "Segunda",
        "Terça",
        "Quarta",
        "Quinta",
        "Sexta", 
        "Sábado"
    ]

#junta os nomes em um único valor
separador = ", " #delimitador
semana = separador.join(dias) #junta os itens da lista

#exibe na tela
print(semana)