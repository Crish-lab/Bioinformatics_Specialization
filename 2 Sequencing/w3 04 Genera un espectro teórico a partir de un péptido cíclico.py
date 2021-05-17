# INPUT: un péptido (en la primera línea de texto y colocar el mismo
# péptido en la línea 43
# OUPUT: una serie de númeeros enteros correspindientes a la masa o
# espectro de dicho péptido

def cyclospectrum(protein):
    # monoisotopic mass table
    mass = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, \
        'E': 129.04259, 'F': 147.06841, 'G': 57.02146, \
        'H': 137.05891, 'I': 113.08406, 'K': 128.09496, \
        'L': 113.08406, 'M': 131.04049, 'N': 114.04293, \
        'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, \
        'S': 87.03203, 'T': 101.04768, 'V': 99.06841, \
        'W': 186.07931, 'Y': 163.06333}

    for aa in mass:
        mass[aa] = int(round(mass[aa]))
    ###

    fragments = [protein]
    cycle = protein * 2
    for i in range(len(protein)):
        for j in range(i + 1, i + len(protein)):
            fragments.append(cycle[i:j])

    spectrum = []
    for fragment in fragments:
        spectrum.append(sum(mass[aa] for aa in fragment))

    string = '0'
    for fragment in sorted(spectrum):
        string += ' ' + str(fragment)

    print(string)
    return string, spectrum


###

f = open("cool_dataset.txt", 'r')
protein = str(f.readline().strip())
protein = 'MTAI'
string, spectrum = cyclospectrum(protein)

f.close()