"""
EXERCÍCIO 11 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
•"Telefonou para a vítima?"
•"Esteve no local do crime?"
•"Mora perto da vítima?"
•"Devia para a vítima?"
•"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

cont = 0
resposta = input("Telefonou para a vítima? ").upper()
if resposta == "SIM" or resposta == "S":
    cont += 1

resposta = input("Esteve no local do crime? ").upper()
if resposta == "SIM" or resposta == "S":
    cont += 1

resposta = input("Mora perto da vítima? ").upper()
if resposta == "SIM" or resposta == "S":
    cont += 1

respota = input("Devia para a vítima? ").upper()
if resposta == "SIM" or resposta == "S":
    cont += 1

resposta = input("Já trabalhou com a vítima? ").upper()
if resposta == "SIM" or resposta == "S":
    cont += 1

if cont == 2:
    print("\nSuspeita")
elif cont == 3 or cont == 4:
    print("\nCúmplice")
elif cont == 5:
    print("\nAssassino")
else:
    print("\nInocente")
