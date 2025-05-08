import os   

chaves = ("nome", "idade", "cpf", "telefone","email", "profissão")

usuario = {
    chaves[0]: "ucas",
    chaves[1]: 25,
    chaves[2]: "123.456.789-00",
    chaves[3]: "(11) 98765-4321",
    chaves[4]: "sjfnbfjnbf",
    chaves[5]: "programador"
}
try:
    while True:
        
        for chave in usuario:
            print(f"{chave}:{usuario.get(chave)}.")
        prosseguir = input("Deseja excluir alguma chave? (s/n): ")
        match prosseguir:
            case "s":
                chave_escolhida = input("Informe a chave que deseja excluir: ")

                if chave_escolhida in chaves:
                    usuario.pop(chave_escolhida, None)
                    os.system("cls")
                    continue
                
                else:
                    os.system("cls")
                    print(f"{chave_escolhida} não existe")
                    continue
            case "n":
                break
            case _:
                print("Opção inválida.")
except Exception as e:
    print(f"Não foi possível atualizar os dados. {e}.")