# INPUT: un número entero correspondiente a la longitud de un péptido cíclico
# es decir, todos los subpéptidos que se encuentran en un péptido:
# NQEL has 12 subpeptides: N, Q, E, L, NQ, QE, EL, LN, NQE, QEL, ELN, and LNQ
# OUPUT: un númeero entero correspindiente a la cantidad de subpéptidos que
# se pueden formar.

#Ingresar el número que se quiere determinar:
number_input = 25875


number_input2 = number_input + 1
answer = number_input2 * number_input
answer = answer / 2
answer = answer + 1
print(answer)