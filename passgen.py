import random
import string
print("---GERADOR DE SENHAS 2.0---")
t = int(input("Defina a quantidade de caracteres: "))
lm = int(input("Defina a quantidade de maiúsculas: "))
ln= int(input("Defina a quantidade de minúsculas: "))
e = int(input("Defina a quantidade de especiais: "))
n = int(input("Defina a quantidade de números: "))
tr = lm + ln + e + n
if tr > t:
    raise ValueError("A soma dos parametros excede o tamanho total solicitado da senha")
def criar_senha(t, lm, ln, e,n):
    m = string.ascii_uppercase
    l = string.ascii_lowercase
    es = "!@#$%&*"
    nu = string.digits
    sen = []
    sen += random.choices(m, k=lm)
    sen += random.choices(l, k=ln)
    sen += random.choices(es, k=e)
    sen += random.choices(nu, k=n)
    r = t - len(sen)
    c = m + l + es + nu
    sen += random.choices(c, k=r)
    random.shuffle(sen)
    return "".join(sen)
senha = criar_senha(t, lm, ln, e, n)
print("Senha gerada com base nos parametros solicitados: ", senha)
