"""
EXERCÍCIO 06 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

for c in range(1, 21):
    print(c)
for c in range(1, 21):
    print(f"{c}, " if c < 20 else f"{c}.", end="")
