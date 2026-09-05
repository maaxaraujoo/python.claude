nota = float(input("Digite uma nota:"))

if nota >= 9:
    print("Ótima nota!")
elif nota >= 7:
    print("Boa nota!")
elif nota >= 5:
    print("Nota regular!")
else:
    print("Nota insuficiente")


# 04.condicionais_elif_multiplas_faixas.py

# QUESTÃO 4
#
# Peça para o usuário digitar uma nota (de 0 a 10) usando
# input(). Usando if, elif e else, exiba um conceito para
# essa nota: "Ótimo" para nota maior ou igual a 9, "Bom"
# para nota maior ou igual a 7, "Regular" para nota maior
# ou igual a 5, e "Insuficiente" para qualquer nota menor
# que 5.
#
# Utilize:
# - input()
# - conversão com float()
# - if
# - elif
# - else
# - print()