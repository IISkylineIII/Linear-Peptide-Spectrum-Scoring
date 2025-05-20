# Linear-Peptide-Spectrum-Scoring

# Description

This Python script calculates the linear score of a peptide against an experimental mass spectrum. It generates the theoretical spectrum of all linear subpeptides from the peptide, compares it to the observed spectrum, and counts the number of matching masses.

# Usage

```

def LinearScore(peptide, spectrum):
    # Generate the theoretical spectrum of the peptide
    theoretical_spectrum = [0]
    n = len(peptide)
    amino_acid_mass = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101,
        'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128,
        'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

    # Generate all subpeptides
    for i in range(n):
        for j in range(1, n - i + 1):
            subpeptide = peptide[i:i+j]
            mass = sum(amino_acid_mass[aa] for aa in subpeptide)
            theoretical_spectrum.append(mass)

    # Sort both spectra
    theoretical_spectrum.sort()
    spectrum.sort()

    # Calculate the linear score
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

# Example usage:
if __name__ == "__main__":
    peptide = "NQEL"
    spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
    result = LinearScore(peptide, spectrum)
    print(result)

```
# Example Output

8

# Applications
* Scoring peptide sequences against experimental mass spectra in proteomics.
* Useful for peptide identification and spectrum matching algorithms.
* Forms a foundational step for de novo peptide sequencing and database searching.

# License
This project is licensed under the MIT License.


