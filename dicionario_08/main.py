#lista de dicionários
pessoas = [
    {
     'nome': 'Alice',
     'idade': 20,
     'email': 'estudos@gmail.com'
     },
    {
        'nome': 'Jessa',
        'idade': 25,
        'email': 'jessa@gmail.com'
    },
     {
        'nome': 'Bingo',
        'idade': 45,
        'email': 'bingo@gmail.com'
    }
]

for pessoa in pessoas:
    print(f"\n{'-'*20}\n")
    for chave in pessoa:
        print(f"{chave.title()}: {pessoa.get(chave)}.")

