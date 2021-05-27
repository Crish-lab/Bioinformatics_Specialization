"""GENERATING THE THEORICAL SPECTRUM OF A PEPETIDE
Code Challenge: Implement LinearSpectrum.

Input: An amino acid string Peptide.
Output: The linear spectrum of Peptide.

Sample Input:
     LEQN
Sample Output:
     0 113 114 128 129 227 242 242 257 355 356 370 371 484

by: jasonmoggridge
# INPUT: UNA PROTEÍNA, PÉPTIDO O CONJUNTO DE AMINOÁCIDOS
# OUTPUT: EL ESPECTRO LINEAL AL CUAL CORRESPONDE DICHA SECUENCIA
"""

def linear_spectrum(peptide):
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(sum(mass[aa] for aa in peptide[i:j]))
    return spectrum
    ##


mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, \
    'N': 114, 'D': 115, 'E': 129, 'K': 128, 'Q': 128, 'M': 131, 'H': 137, 'F': 147, \
    'R': 156, 'Y': 163, 'W': 186 \
    }
##
# INGRESAR EL PÉPTIDO A ANALIZAR:
peptide = 'TFRDGMDPWVQGDLNHFRMASNGTDAIIMGYPKPERI'

spec = linear_spectrum(peptide)
string = ''
for mass in sorted(spec):
    string += str(mass) + ' '

print(string)