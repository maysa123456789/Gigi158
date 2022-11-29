'''
#1e n1
total = 0
for i in range(1,7,1):
    nu = int(input("Informe um número inteiro:"))
    if nu % 2 == 0:
        continue
    elif nu % 2 == 1:
        total = total + nu
print(total)

#correçao
contador = 0
for i in range(5):
    peso = int(input("Imforme o peso:"))
    if peso >= 80:
        contador = contador + 1
print(contador, "pessoas com mais de 80kg")
'''
contador = 0
maior_deposito = 0.0
while True:
    n = int(input("Informe uma opção:"))
    if n == 1:
        print("Seu saldo é de", contador)
    elif n == 2:
        dep = float(input("Quanto quer depositar:"))
        contador = contador + dep
        if dep > maior_deposito:
            maior_deposito = dep
    elif n == 3:
        saq = float(input("Quanto quer sacar:"))
        contador = contador - saq
        print("Seu saldo agora é de", contador)
    elif n == 4:
        import random
        sorteio = random.randint(1,2)
        if sorteio == 1:
            contador = contador * 2
            print("Parabéns! Você teve sorte, seu saldo agora é de", contador)
        if sorteio == 2:
            contador = contador / 2
            print("Você teve azar. Seu saldo agora é de", contador)
    elif n == 5:
         break
    print("Seu saldo agora é de", dep)
