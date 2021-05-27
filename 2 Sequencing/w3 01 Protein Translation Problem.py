"""PROTEIN TRANSLATION PROBLEM
Translate an RNA string into an amino acid string.

Input: An RNA string Pattern and the array GeneticCode.
Output: The translation of Pattern into an amino acid string Peptide.

Sample Input:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output:
MAMAPRTEINSTRING

by: jasonmoggridge
"""


def TranslateRNA(rna):
    """ Creates codon_table, then parses RNA into Codons for lookup,
    aminoacids are appended to the string protein and returned
    """
    rna = rna.lower().replace('\n', '').replace(' ', '')

    ### codon table ###

    bases = ['u', 'c', 'a', 'g']
    codons = [a + b + c for a in bases for b in bases for c in bases]
    aminoacids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, aminoacids))

    ### codon lookup ###

    pos = 0
    protein = ''
    while pos < len(rna) - 2:
        codon = rna[pos:pos + 3]
        for key in codon_table:
            if codon == key:
                if codon_table[key] != '*':
                    protein = protein + codon_table[key]
                    pos += 3
                else:
                    pos += 3
                    break
    return (protein)


infile = open('cool_dataset.txt', 'r')
rna = infile.read()

# test case # rna ="AUGCGUA"

prot = TranslateRNA(rna)
print(str(prot))

output = open("cool_dataset.txt", 'w')
output.write(prot)
output.close()