#O SPLIT serpara os valores de uma variável em uma lista

#variavel
ano = "January, February, March, April, May, June, July, August, September, October, November, December"

#algoritimo
try:
    meses = ano.split(", ")
    for mes in meses:
        print(mes)
except Exception as e:
    print(f"Não foi possível separar os valores. {e}.")