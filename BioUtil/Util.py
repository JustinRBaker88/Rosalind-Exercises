# Read a FASTA formatted text file containing DNA strings from Rosalind and
# returns an array of corresponding DNA strings. Takes a file path as a parameter.
def parse_fasta(fasta_path):
    parsed = []
    data = open(fasta_path,'r')
    
    index = -1
    for line in data:
        if (line[0] == '>'):
            parsed.append("")
            index += 1
        else:
            parsed[index] += line.strip()
    
    data.close()
    return parsed

# Accepts two parameters and returns a corresponding DNA K-Mer string
# Index represents the order of the K-Mer and k represents the number
# bases in the K-Mer. 
def get_dna_kmer(index, k):
    kmer = []
    nucleobase = ["A", "C", "T", "G"]
    
    for x in range(k):
        kmer.append(nucleobase[0])
    
    for i in range(k-1, -1, -1):
        kmer[i] = nucleobase[int(index % 4)]
        index = int(index/4)
        
    return "".join(kmer)
