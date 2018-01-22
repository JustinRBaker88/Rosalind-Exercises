# Read a FASTA formatted text file containing DNA strings from Rosalind and
# returns an array of corresponding DNA strings. Takes a file path as a parameter.
def parse_fasta(fasta_path):
    parsed = []
    data = open(fasta_path,'r')
    
    temp_dna = ""
    index = -1
    for line in data:
        if (line[0] == '>'):
            parsed.append("")
            index += 1
        else:
            parsed[index] += line.strip()
    
    data.close()
    return parsed