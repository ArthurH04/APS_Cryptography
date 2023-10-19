import os

def criptografia(texto, chave):
    texto_cifrado = ""
    for i in range(len(texto)):
        texto_cifrado += chr(ord(texto[i]) ^ ord(chave[i % len(chave)]))
    return texto_cifrado

def descriptografar(texto_cifrado, chave):
    return criptografia(texto_cifrado, chave)


diretorioCorrentee = os.getcwd()

with open('-', 'r', encoding='utf-8') as acesso:
    acesso.read

with open('-', 'r', encoding='utf-8') as arq:
    arquivo_criptografado = criptografia(arq.read(),str(acesso))
    print(arquivo_criptografado)

with open('-', 'w+', encoding='utf-8') as arq2:
    arq2.write(arquivo_criptografado)
    arq2.seek(0)
    print(descriptografar(arq2.read(), str(acesso)))