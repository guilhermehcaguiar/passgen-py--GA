import random
import string
print("---GERADOR DE SENHAS 1.0---")
t = int(input("Defina a quantidade caracteres:"))
def criar_senha(t):
    c = string.ascii_letters + string.digits + string.punctuation
    s = "".join(random.choice(c) for _ in range (t))
    return s
sen = criar_senha(t)
print("Senha:", sen)
