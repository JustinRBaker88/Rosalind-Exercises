from BioUtil import Util
from BioUtil.Util import get_dna_kmer

def motif_enumeration(Dna, k, d):
    patterns = set()
    # Search each K-Mer possible in DNA
    for x in range(4**k):
        pattern = get_dna_kmer(x, k)
        
        # TODO: Possible improvement, have function return multiple matching motifs
        if (matching_kmer(pattern, d, Dna)):
            patterns.add(pattern)
            
    return patterns



def matching_kmer(kmer, min_score, DNA):
    k = len(kmer)

    for strands in DNA:
        min_strand_score = k
        for i in range(k -1, len(strands)):
            sub_score = 0
            for j in range(k):
                if (kmer[j] != strands[i-k+j+1]):
                    sub_score += 1
            if (sub_score < min_strand_score):
                min_strand_score = sub_score
            sub_score = 0
        if (min_strand_score > min_score):
            return False         
    return True

def parse_data(path):
    parsed = []
    data = open(path,'r')
    
    index = 0
    for line in data:
        if (index == 0):
            args = line.split()
            parsed.append(int(args[0]))
            parsed.append(int(args[1]))
        else:
            parsed.append(line.strip())
        index +=1
    
    data.close()
    return parsed

path = "./data.txt"

parse_results = parse_data(path)

k = parse_results[0]
d = parse_results[1] 
dna = parse_results[2:]       

motifs = motif_enumeration(dna , k, d)

for x in motifs:
    print(x + " ", end="") 