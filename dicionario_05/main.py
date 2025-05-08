chaves = ("nome", "idade", "cpf", "telefone","email", "profissão")

usuario = {
    chaves[0]: "ucas",
    chaves[1]: 25,
    chaves[2]: "123.456.789-00",
    chaves[3]: "(11) 98765-4321",
    chaves[4]: "sjfnbfjnbf",
    chaves[5]: "programador"
}
for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}")