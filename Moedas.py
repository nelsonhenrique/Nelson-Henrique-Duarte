import os
import sys, traceback
qtd05 = 0
qtd025 = 0
qtd01 = 0
qtd005 = 0
qtd001 = 0
qtd1 = 0
qtd2 = 0
qtd5 = 0
qtd10 = 0
qtd20 = 0
qtd50 = 0
qtd100 = 0
saque = float(input(""))


if saque >= 100:
    qtd100 = saque//100
    saque = saque - qtd100*100

if saque >= 50:
    qtd50 = saque//50
    saque = saque - qtd50*50

if saque >= 20:
    qtd20 = saque//20 
    saque = saque - qtd20*20

if saque >= 10:
    qtd10 = saque//10
    saque = saque - qtd10*10

if saque >= 5:
    qtd5 = saque//5
    saque = saque - qtd5*5

if saque >= 2:
    qtd2 = saque//2
    saque = saque - qtd2*2

if saque >= 1:
    qtd1 = saque//1
    saque = saque - qtd1*1

if saque >= 0.5:
    qtd05 = saque//0.5
    saque = saque - qtd1*0.5

if saque >= 0.25:
    qtd025 = saque//0.25
    saque = saque - qtd1*0.25

if saque >= 0.1:
    qtd01 = saque//0.1
    saque = saque - qtd1*0.1

if saque >= 0.05:
    qtd005 = saque//0.05
    saque = saque - qtd1*0.05

if saque >= 0.01:
    qtd001 = saque//0.01
    saque = saque - qtd1*0.01




print(qtd100, "Nota(s) de R$ 100.00")
print(qtd50, "Nota(s) de R$ 50.00: ")
print(qtd20, "Nota(s) de R$ 20.00: ")
print(qtd10, "Nota(s) de R$ 10.00: ")
print(qtd5, "Nota(s) de R$ 5.00: ")
print(qtd2, "Nota(s) de R$ 2.00: ")
print(qtd1, "Moeda(s) de R$ 1.00: ")
print(qtd05, "Moeda(s) de R$ 0.50: ")
print(qtd025,"Moeda(s) de R$ 0.25: ")
print(qtd01, "Moeda(s) de R$ 0.10: ")
print(qtd005, "Moeda(s) de R$ 0.05: ")
print(qtd001, "Moeda(s) de R$ 0.01: ")


os.system("pause")













    

