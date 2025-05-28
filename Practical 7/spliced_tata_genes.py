import re

def read_fasta(file_path):
    genes = {}
    current_gene = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_gene is not None:
                    genes[current_gene]['sequence'] = ''.join(genes[current_gene]['sequence'])
                current_gene = extract_gene_id(line[1:])
                genes[current_gene] = {
                    'header': line,
                    'sequence': []
                }
            else:
                if current_gene is not None:
                    genes[current_gene]['sequence'].append(line)
        if current_gene is not None:
            genes[current_gene]['sequence'] = ''.join(genes[current_gene]['sequence'])
    return genes
# This script finds genes with specific splice sites and TATA box sequences in a FASTA file.
def extract_gene_id(header):

    match = re.search(r'gene:([^\s;]+)', header) or \
            re.search(r'ID=([^\s;]+)', header) or \
            re.search(r'>([^\s]+)', header)
    return match.group(1) if match else header.split()[0]
# This function searches for genes with specific splice sites and TATA box sequences.
def find_spliced_genes_with_tata(genes_dict, splice_pattern):
    result = {}
    splice_re = re.compile(f'GT.*{splice_pattern}')  
    tata_re = re.compile(r'TATAA[AT]|TATATA', re.IGNORECASE)  
    
    for gene_id, data in genes_dict.items():
        sequence = data['sequence']
        if splice_re.search(sequence):
            tata_matches = tata_re.findall(sequence)
            if tata_matches:
                result[gene_id] = {
                    'sequence': sequence,
                    'count': len(tata_matches)
                }
    return result
# This function writes the results to a new FASTA file.
def write_fasta(output_path, sequences_dict):
    with open(output_path, 'w') as file:
        for gene_id, data in sequences_dict.items():
            file.write(f'>{gene_id} TATA_count={data["count"]}\n')
            file.write(f'{data["sequence"]}\n')
# Main function to execute the script.
def main():
    print("Available splice modes: GTAG, GCAG, ATAG")
    while True:
        splice_pattern = input("Please enter the splice mode: ").upper()
        if splice_pattern in ['GTAG', 'GCAG', 'ATAG']:
            break
        print("If the input is invalid, select GTAG, GCAG, or ATAG")

    input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_file = f"{splice_pattern}_spliced_genes.fa"
# This script reads a FASTA file, finds genes with specific splice sites and TATA box sequences, and writes the results to a new FASTA file.
    genes = read_fasta(input_file)
    matched_sequences = find_spliced_genes_with_tata(genes, splice_pattern)
    write_fasta(output_file, matched_sequences)

    print(f" {len(matched_sequences)} matching genes found, and the results are saved to {output_file}")
# This script is designed to find genes with specific splice sites and TATA box sequences in a FASTA file.
if __name__ == "__main__":
    main()