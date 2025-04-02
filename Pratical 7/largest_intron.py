seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

def find_largest_intron(sequence):
    max_length = 0
    for i in range(len(sequence)-3):
        if sequence[i] == 'G' and sequence[i+1] == 'T':
            for j in range(i+2, len(sequence)-1):
                if sequence[j] == 'A' and sequence[j+1] == 'G':
                    intron_length = j - i + 2  
                    if intron_length > max_length:
                        max_length = intron_length
                        break
    
    return (max_length)

# Analyze the sequence
max_len = find_largest_intron(seq)

print(max_len)
