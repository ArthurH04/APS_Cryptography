import os

def criptografia(texto, chave):
    texto_cifrado = ""
    for i in range(len(texto)):
        texto_cifrado += chr(ord(texto[i]) ^ ord(chave[i % len(chave)]))
    return texto_cifrado

def descriptografar(texto_cifrado, chave):
    return criptografia(texto_cifrado, chave)


diretorioCorrentee = os.getcwd()

with open('C:/Users/Pichau/OneDrive/Documentos/estudos/2semestre-facul/APS/Arquivo01.txt', 'r', encoding='utf-8') as arq:
    print(criptografia(arq.read(), '1000'))

with open('C:/Users/Pichau/OneDrive/Documentos/estudos/2semestre-facul/APS/Arquivo02.txt', 'r', encoding='utf-8') as arq2:
    print(descriptografar(arq2.read(), '1000'))