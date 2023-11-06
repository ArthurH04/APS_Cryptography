import os

def criptografia(texto, chave):
    texto_cifrado = ""
    for i in range(len(texto)):
        texto_cifrado += chr(ord(texto[i]) ^ ord(chave[i % len(chave)]))
    return texto_cifrado

def descriptografar(texto_cifrado, chave):
    return criptografia(texto_cifrado, chave)

def verificarChave(chave):
    if chave.isdigit():
        return True
    else:
        print("\n")
        print("*"*100)
        print("A chave deve conter apenas números.")
        print("*"*100)
        return False 

def verificaQuantidadeCaracteres(text):
    if (len(text) > 128):
        print("\n")
        print("*"*100)
        print("O texto deve conter até 128 caracteres.")
        print("*"*100)
        return False
    return True

def verificaExtensao(diretorioArquivo):
    if diretorioArquivo.endswith('.txt'):
        return False
    else:
        print("\n")
        print("*"*100)
        print("A extensão do arquivo deve ser .txt")
        print("*"*100)
        return True

def diretorioDestinoVazio(diretorio):
    if diretorio == "":
        print("\n")
        print("*"*100)
        print("O diretório não pode estar vazio")
        print("*"*100)
        return True
    else:
        return False
    
def nomeArquivoVazio(nome):
    if nome == "":
        print("\n")
        print("*"*100)
        print("O nome do arquivo não pode estar vazio")
        print("*"*100)
        return True
    else:
        return False

while True:
    
    escolha = None
    while escolha is None:
        try:
            print("\nO que você deseja fazer?")
            escolha = int(input("Criptografar - 1\nDescriptografar - 2\nInstruções - 3\n"))
        except ValueError:
            print("Por favor, insira um número válido.")

    match escolha:
        case 1:
            print("\n----Criptografando----\n")

            while True:
                diretorioArquivo = input("Digite o diretório do arquivo .txt que você deseja criptografar: \n")

                if not verificaExtensao(diretorioArquivo):
                    with open(diretorioArquivo, 'r', encoding='utf-8') as arq:
                        text = arq.read()
                    if verificaQuantidadeCaracteres(text):
                        break

            while True:
                diretorioAcesso = input("Digite o diretório do arquivo .txt que contém a senha de acesso: \n")
                if not verificaExtensao(diretorioAcesso):
                    with open(diretorioAcesso, 'r', encoding='utf-8') as acesso:
                        key = acesso.read()
                        if verificarChave(key):
                            arquivoCriptografado = criptografia(text,str(key))
                            break

            while True:
                diretorioDestino = input("Digite o diretório destino do arquivo criptografado: \n")
                if not diretorioDestinoVazio(diretorioDestino):
                    break

            while True:
                arquivoCriptografadoNome = input("Digite o nome do arquivo que será criptografado: \n")
                if not nomeArquivoVazio(arquivoCriptografadoNome):
                    break

            with open(diretorioDestino + arquivoCriptografadoNome + ".txt", 'w+', encoding='utf-8') as arqCripto:
                arqCripto.write(arquivoCriptografado)
                arqCripto.seek(0)


            os.remove(diretorioArquivo)
            os.remove(diretorioAcesso)

        case 2:
            print("\n----Descriptografando----\n")

            while True:
                diretorioArquivoCripto = input("Digite o diretório do arquivo .txt que você deseja descriptografar: \n")

                if not verificaExtensao(diretorioArquivoCripto):
                    break
                
            while True:
                diretorioAcesso = input("Digite o diretório do arquivo .txt que contém a senha de acesso: \n")
                if not verificaExtensao(diretorioAcesso):
                    break

            while True:
                diretorioDestino = input("Digite o diretório destino do arquivo descriptografado: \n")
                if not diretorioDestinoVazio(diretorioDestino):
                    break

            while True:
                arquivoDescriptografadoNome = input("Digite o nome do arquivo descriptografado: \n")
                if not nomeArquivoVazio(arquivoCriptografadoNome):
                    break

            with open(diretorioAcesso, 'r', encoding='utf-8') as acesso:
                key = acesso.read()

            with open(diretorioArquivoCripto, 'r', encoding='utf-8') as arqCripto:
                arquivoCriptografado = arqCripto.read()
            
            arquivoDescriptografado = descriptografar(arquivoCriptografado, key)

            with open(diretorioDestino + arquivoDescriptografadoNome + ".txt", "w+", encoding='utf-8' ) as arqDescripto:
                arqDescripto.write(arquivoDescriptografado)
                arqDescripto.seek(0)
                            
            os.remove(diretorioArquivoCripto)
            os.remove(diretorioAcesso)

        case 3:
            print("")
            print("*"*100)
            print("""O arquivo de texto a ser criptografado e a senha devem estar em um arquivo '.txt'
O texto deve conter até 128 caracteres""")
            print("""
⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️
Após criptografar, o texto e a chave serão removidos! Lembre-se bem da chave!
Após descriptografar o texto, o texto criptografado e a chave também serão removidos!
⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️""")
            print("*"*100)
        case _:
            print("Opção inválida.")

    continuar = input("\nDeseja (F)echar o programa ou (C)ontinuar criptografando/descriptografando?\n")
    if continuar.upper() == 'F':
        break