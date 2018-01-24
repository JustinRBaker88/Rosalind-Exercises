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
        
dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
motifs = motif_enumeration(dna , 3, 1)

for x in motifs:
    print(x + " ", end="") 