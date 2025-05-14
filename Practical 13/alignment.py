import os

from Bio.Align import substitution_matrices
from Bio.SeqIO import read

def read_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if not line.startswith('>') and line.strip()]
    seq = ''.join(lines)
    if not seq:
        raise ValueError(f"There are no valid sequences in the file")
    return seq

blosum = substitution_matrices.load("BLOSUM62")
def compare(seq1, seq2, blosum):
    score = 0
    identical = 0
    for a, b in zip(seq1, seq2):
        if (a, b) not in blosum: 
            raise ValueError(f"Amino acid pairs  {a}↔{b} are not in the BLOSUM62 matrix!")
        score += blosum[(a, b)]
        if a == b:
            identical += 1
    identity_percent = (identical / len(seq1)) * 100
    return score, identity_percent
if __name__ == "__main__":

    required_files = ["SOD2_HUMAN.fasta", "SOD2_MOUSE.fasta", "RANDOM.fasta", "BLOSUM62.txt"]
    for file in required_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"The required documents {file}were not found")


    human_seq = read_fasta("SOD2_HUMAN.fasta")
    mouse_seq = read_fasta("SOD2_MOUSE.fasta")
    random_seq = read_fasta("RANDOM.fasta")
   

    comparisons = [
        ("Human vs Mouse", human_seq, mouse_seq),
        ("Human vs Random", human_seq, random_seq),
        ("Mouse vs Random", mouse_seq, random_seq)
    ]

    for name, seq1, seq2 in comparisons:
        print(f"\n{name}:")
        print(f"seq1 length: {len(seq1)}, seq2 length: {len(seq2)}")
        try:
            score, identity = compare(seq1, seq2, blosum)
            print(f"Compare scores: {score}")
            print(f"Identity percentage: {identity:.2f}%")
        except ValueError as e:
            print(f"error: {e}")