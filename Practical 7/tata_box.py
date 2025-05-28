import re

def read_fasta(file_path):
    genes = {}
    current_gene = None
    with open(file_path, 'r') as file:# Open the FASTA file for reading
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_gene is not None:# If we have a current gene, save its sequence
                    genes[current_gene] = ''.join(genes[current_gene])
                current_gene = extract_gene_id(line[1:]) 
                genes[current_gene] = []
            else:# If the line is a sequence line, append it to the current gene's sequence
                if current_gene is not None:
                    genes[current_gene].append(line)
        if current_gene is not None:
            genes[current_gene] = ''.join(genes[current_gene])
    return genes
# This script finds genes with TATA box sequences in a FASTA file.
def extract_gene_id(header):
    match = re.search(r'gene:(\S+)', header)
    return match.group(1) if match else header  
# This function finds genes with TATA box sequences in a dictionary of gene sequences.
def find_tatawaw_sequences(genes_dict):
    pattern = re.compile(r'TATA[AT]A[AT]')  
    return {k: v for k, v in genes_dict.items() if pattern.search(v)}
# This function writes the matched sequences to a new FASTA file.
def write_fasta(output_path, sequences_dict):
    with open(output_path, 'w') as file:
        for gene_id, sequence in sequences_dict.items():
            file.write(f'{gene_id}\n{sequence}\n')  
# Main function to execute the script.

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"        
output_file = "tata_genes.fa"     

genes = read_fasta(input_file)


matched_sequences = find_tatawaw_sequences(genes)


write_fasta(output_file, matched_sequences)

print(f" {len(matched_sequences)}{output_file}")