'''
Solve the String Composition Problem
 Input: un número entero "K" y un string "text" de la secuencia a analizar
 Output: una serie de secuencias obtenidas de la secuencia previa con el tamaño
 del número entero que ingresamos

Sample Input:
5
CAATCCAAC
Sample Output:
CAATC
AATCC
ATCCA
TCCAA
CCAAC
'''


k = 5
text = "CAATCCAAC"
print(*(sorted([text[i:i+k] for i in range(len(text) - k + 1)])), sep = '\n')