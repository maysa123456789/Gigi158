#jogodavelha
import random

def inicia():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Você iniciou o jogo")
    while True:
        tabuleiro(lista)
        print(lista)
        game1 = int(input("Jogador 1, escolha a posição que deseja:"))
        if observa(lista, game1): 
            continue
        lista[game1 - 1]= "x"
        sorteio = random.randint(1,9)
        print("Jogador 2 escolheu a posição", sorteio)   
        if sorteio == game1:
            continue
        lista[sorteio - 1] = "o"
        
        
        


def sair():
  quit()


def menu():
  print("Bem vindo ao jogo da velha\n Você possui dua opções")
  print("1.Iniciar o jogo \n 2.Sair")
  a = int(input("Escolha alguma delas:"))
  if a == 1:
      inicia()
  if a == 2:
      sair()
  
def tabuleiro(lista: list):
  print()
  print("", lista[6],"|", lista[7],"|", lista[8], "")
  print("---|---|---")
  print("", lista[3],"|", lista[4],"|", lista[5], "")
  print("---|---|---")
  print("", lista[0],"|", lista[1],"|", lista[2])

def observa(lista,posicao):
    if lista[posicao] == "x" or lista[posicao] == "o":
        print("Posição ocupada")
        return True
    return False
    

menu()

  

