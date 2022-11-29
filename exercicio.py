'''
def exercicio9(dia_parametro):
    if dia_parametro == "segunda" or dia_parametro == "terça":
        emoji = ":("
    elif dia_parametro == "quarta" or dia_parametro == "quinta":
        emoji = ":|"
        
    elif dia_parametro == "sexta" or dia_parametro == "sábado" or dia_parametro == "domingo":
        emoji = ":)"
    else:
        print("Esse dia não existe")
       
    return emoji
        
dia = input("Informe o dia:")
emoji_fora = exercicio9(dia)
print(emoji_fora)

while True:
    n = int(input("Informe um valor:"))
    
    print(n**2)

    if n == 0:
        break
'''
dentro = 0
fora = 0
for i in range(5):
    n = int(input("Informe o valor:"))
    
    if n >= 10 and n <= 20:
        dentro  





























































