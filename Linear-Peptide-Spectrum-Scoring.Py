def LinearScore(peptide, spectrum):
    theoretical_spectrum = [0]
    n = len(peptide)
    amino_acid_mass = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101,
        'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128,
        'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

    for i in range(n):
        for j in range(1, n - i + 1):
            subpeptide = peptide[i:i+j]
            mass = sum(amino_acid_mass[aa] for aa in subpeptide)
            theoretical_spectrum.append(mass)

    theoretical_spectrum.sort()
    spectrum.sort()

    score = 0
    i, j = 0, 0
    while i < len(theoretical_spectrum) and j < len(spectrum):
        if theoretical_spectrum[i] == spectrum[j]:
            score += 1
            i += 1
            j += 1
        elif theoretical_spectrum[i] < spectrum[j]:
            i += 1
        else:
            j += 1

    return score

if __name__ == "__main__":
    peptide = "NQEL"
    spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
    result = LinearScore(peptide, spectrum)
    print(result)
