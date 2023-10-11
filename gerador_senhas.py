import random

senha = ""

caracteres = "abcdefghijklmnopqrstuvwxyz1234567890!"

for digito in range(16):
    aleatorio = random.choice(caracteres)
    senha += aleatorio

print("=-"*30)
print(senha)
print("=-"*30)