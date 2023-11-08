from hashlib import md5 
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def cripto_1(): #criptografia com hash 
    chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista".encode("utf8")

    hash = md5(chave_secreta).hexdigest()

    print(f"Criptografia com HASH: {hash}")
    print("\n\n")

def cripto_2(): # criptografia com fernet

    chave = b"#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"
    chave = Fernet.generate_key()
    fernet= Fernet(chave)
    value_key= fernet.encrypt(chave) 

    print(f"Criptografia com Fornet:  {value_key.decode()}")
    print("\n\n")

def cripto_3(): #criptografia com algoritmo de rsa
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    chave_publica= chave_privada.public_key()

    chave = b"#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"

    senha = chave_publica.encrypt(
        chave, 
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label= None
        )
    )

    print(f"Criptografia com RSA:  {senha}")


cripto_1()
cripto_2()
cripto_3()


    



