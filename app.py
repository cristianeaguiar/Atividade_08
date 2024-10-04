# tupla
atributos = ("Nome", "Idade", "CPF" , "E-mail", "Profissão", "Tipo Sanguíneo" , "Peso", "Altura")

# lista de dicionarios
usuarios = [] 

# loop
while True:
    #menu
    print("1 - Cadastre novo Usuário.")
    print("2 - Exibir lista.") 
    # usuário informa a opção deseja 
    opcao = input("opção desejada: ")
# Limpa console
    os.system("cls")

# program verifica a opção escolhidapelo usuário
    match opcao:
        case "1":
            novo_usuario = input("Informe os dados a serem cadastrados:")
           usuario.append(novo_usuario)
            print(f"{novo_usuario} cadastrado com sucesso!")
            continue
        case "2":
            print("Lista:\n")
            for i in range(len(nomes)):
                print(f"Índice {i}: {nomes[i]}.")
            print("\n")
            continue   
# cadastrar um novo usuário
usuario = {}

for atributo in atributos:
    usuario[atributo] = input(f"Informe o valor do campo {atributo}: ")
usuarios.append(usuario)

# exibir os dados de cada usuário
for usuario in usuarios:
    print(" ")
    for atributo in atributos:
        print(f"{atributo}: {usuario.get(atributo)}.")
       
print(" ")