#TODO: Crie um programa em que o usuário informa várias notas de um aluno de 0 a 10 (quantas notas quiser adicionar), e ao final, o programa calcule a média desse aluno e informe se ele está aprovado, reprovado ou de recuperação. Obs: a média para aprovação é 7. Recuperação entre 5 e 7. Abaixo de 5 reprovado.

import os 

#replace virgula por ponto + variáveis
nota1 = float(input("Informe uma nota: ").replace(",", "."))
continuar = input("Deseja inserir mais uma nota? (s/n): ") #pergunta se o usuário deseja inserir uma nova nota
nota2 = float(input("Informe uma nota: ").replace(",", "."))
continuar = input("Deseja inserir mais uma nota? (s/n): ") #pergunta se o usuário deseja inserir uma nova nota
nota3 = float(input("Informe uma nota: ").replace(",", "."))
sum(print(f"Soma os numeros da lista: {sum(nota1, nota2)}."))

print(f"{nota}) - {type(nota)}")



    

# faz as médias as notas inseridas


#insere o loop
if nota1 >= 7:
    print(f"Aluno Aprovado")
if nota1 >5:
    print(f"Aluno Recuperação")
else:
    print(f"Reprovado")
    

print(situacao) 

#print