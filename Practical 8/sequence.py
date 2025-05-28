def find_the_place(sequence, target):
    standard_nucleotides = ['A','C','G','T']
    for nucleotide in sequence:
        if nucleotide not in standard_nucleotides:
            print("Error: DNA sequence contains non-canonical nucleotides.")
            return None
       # Check if the target sequence contains only standard nucleotides
    for nucleotide in target:
        if nucleotide not in standard_nucleotides:
            print("Error: DNA sequence contains non-canonical nucleotides.")
            return None
        # Check if the target sequence is longer than the DNA sequence
    DNA_sequence = sequence.upper()
    Target_sequence = target.upper()
# Check if the target sequence is longer than the DNA sequence
    
    len_DNA_sequence = len(DNA_sequence)
    len_Target_sequence = len(Target_sequence)
    for i in range(len_DNA_sequence - len_Target_sequence + 1):# Loop through the DNA sequence to find the target sequence
        if DNA_sequence[i:i + len_Target_sequence] == Target_sequence:
              # If a match is found, print the position (1-based index)
            print(f"Found at position: {i + 1}")
    if not position:    
        print("No match found")
        return None
    
# Main program to get user input and call the function
x = input("Enter the DNA sequence: ")
x = x.upper()
y = input("Enter the target sequence: ")
y = y.upper()
find_the_place(x, y)