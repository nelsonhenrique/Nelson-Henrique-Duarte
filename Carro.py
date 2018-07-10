import os
import sys, traceback

class carro(object):
    ano = []
    velo = []

def exibirMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Inserir carro?")
    c = input("'S' ou 'N'?: ")
    if c == "n" or c == "N":
        print("Finalizado!")
    elif c == "s" or c == "S":
        inserirCarro()


def inserirCarro():
    os.system('cls' if os.name == 'nt' else 'clear')
    a = int(input("Ano: "))
    carro.ano.append(a) 
    v = int(input("Velocidade: "))
    carro.velo.append(v)
    cont = input("Continuar? 'S' ou 'N': ")
    if cont == "N" or cont == "n":
        print("Finalizado!")
    elif cont == "S" or cont == "s":
        exibirMenu()


def exibirDados():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Carro mais novo: ", max(carro.ano))
    print("Maior velocidade: ", max(carro.velo))
    print("Média de velocidade: ", sum(carro.velo)/len(carro.velo))
    os.system("pause")
    
    
exibirMenu()
exibirDados()

