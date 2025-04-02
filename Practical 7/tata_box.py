import re

def read_fasta(file_path):
    genes = {}
    current_gene = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_gene is not None:
                    genes[current_gene] = ''.join(genes[current_gene])
                current_gene = extract_gene_id(line[1:]) 
                genes[current_gene] = []
            else:
                if current_gene is not None:
                    genes[current_gene].append(line)
        if current_gene is not None:
            genes[current_gene] = ''.join(genes[current_gene])
    return genes

def extract_gene_id(header):
    match = re.search(r'gene:(\S+)', header)
    return match.group(1) if match else header  

def find_tatawaw_sequences(genes_dict):
    pattern = re.compile(r'TATA[AT][AT]')  
    return {k: v for k, v in genes_dict.items() if pattern.search(v)}

def write_fasta(output_path, sequences_dict):
    with open(output_path, 'w') as file:
        for gene_id, sequence in sequences_dict.items():
            file.write(f'{gene_id}\n{sequence}\n')  


input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"        
output_file = "tata_genes.fa"     

genes = read_fasta(input_file)


matched_sequences = find_tatawaw_sequences(genes)


write_fasta(output_file, matched_sequences)

print(f" {len(matched_sequences)}{output_file}")