'''CYCLOPEPTIDE SCORING PROBLEM
Compute the score of a cyclic peptide against a spectrum.

Input: An amino acid string Peptide and a collection of integers Spectrum.
Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).

________________________________＊ 　 ｡*　　+　 　＊ 　･ ｡☆_________________________________________
 El espectro experimental difiere del espectro real del péptido, el SCORE
 es la cantidad de elementos similares que el expectro experimental comparte
 con el péptido

 INPUT: el péptido en su forma alfabética (por cada aminoácido) y el espectro experimental
 (que es la serie numérica)
   En el doc. de texto primera línea el péptido en su forma ALFABÉTICA, y en la segunda
   línea la secuencia numérica del expectro con espacios sin comas.
 OUPUT: un número entero equivalente al número de coincidencias o matches del espectro
 con el péptido real.

Sample Input:
NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484
Sample Output:
11
'''

mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, \
    'N': 114, 'D': 115, 'E': 129, 'K': 128, 'Q': 128, 'M': 131, 'H': 137, 'F': 147, \
    'R': 156, 'Y': 163, 'W': 186 \
    }


##


def cyclospectrum(protein):
    spec = [0, int(sum(mass[aa] for aa in protein))]
    cycle = protein * 2

    for i in range(len(protein)):
        for j in range(i + 1, i + len(protein)):
            spec.append(sum(mass[aa] for aa in cycle[i:j]))

    return spec


###

def score(peptide, spectrum):
    score = 0
    for fragment in cyclospectrum(peptide):
        if fragment in spectrum:
            score += 1
            spectrum.remove(fragment)
    return score



f = open("cool_dataset.txt", 'r')
peptide = str(f.readline().strip())
experimental = [int(i) for i in f.readline().split(' ')]
print(score(peptide,experimental))

#peptide = 'MAMA'
#experimental = [0, 71, 71, 71, 131, 131, 131, 156, 198, 199, 202, 202, 202, 333, 333, 333, 404, 404]
#score = score(peptide, experimental)
