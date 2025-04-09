def find_the_place(sequence, target):
    standard_nucleotides = ['A','C','G','T']
    for nucleotide in sequence:
        if nucleotide not in standard_nucleotides:
            print("Error: DNA sequence contains non-canonical nucleotides.")
            return None
        
    for nucleotide in target:
        if nucleotide not in standard_nucleotides:
            print("Error: DNA sequence contains non-canonical nucleotides.")
            return None
        
    DNA_sequence = sequence.upper()
    Target_sequence = target.upper()

    position = []
    len_DNA_sequence = len(DNA_sequence)
    len_Target_sequence = len(Target_sequence)
    for i in range(len_DNA_sequence - len_Target_sequence + 1):
        if DNA_sequence[i:i + len_Target_sequence] == Target_sequence:
            position.append(i + 1)  
            print(f"Found at position: {i + 1}")
    if not position:    
        print("No match found")
        return None
    
        
        
x = input("Enter the DNA sequence: ")
x = x.upper()
y = input("Enter the target sequence: ")
y = y.upper()
find_the_place(x, y)