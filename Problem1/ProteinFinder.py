from BioUtil import Util

protein_translation =  {"UUU" : "F", "UUC" : "F", "UUA" : "L", "UUG" : "L",
                        "CUU" : "L", "CUC" : "L", "CUA" : "L", "CUG" : "L",
                        "AUU" : "I", "AUC" : "I", "AUA" : "I", "AUG" : "M",
                        "GUU" : "V", "GUC" : "V", "GUA" : "V", "GUG" : "V",
                        "UCU" : "S", "UCC" : "S", "UCA" : "S", "UCG" : "S",
                        "CCU" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P",
                        "ACU" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T",
                        "GCU" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A",
                        "UAU" : "Y", "UAC" : "Y", "UAA" : "-", "UAG" : "-",
                        "CAU" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q",
                        "AAU" : "N", "AAC" : "N", "AAA" : "T", "AAG" : "K",
                        "GAU" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E",
                        "UGU" : "C", "UGC" : "C", "UGA" : "-", "UGG" : "W",
                        "CGU" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R",
                        "AGU" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R", 
                        "GGU" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"}

def dna_to_rna(dna_string):
    rna = []
    for basepairs in dna_string :
        if (basepairs == "T"):
            rna.append("U")
        else:
            rna.append(basepairs) 
            
    return "".join(rna)

def remove_introns(dna, introns):
    for x in introns :
        index = dna.index(x)
        dna = dna[0:index] + dna[index+len(x):]
    return dna

def print_proteins(rna):
    for i in range (0, len(rna) -1, 3) :
        if (len(rna[i:i+3]) == 3) :
            if (protein_translation[rna[i:i+3]] == "M" and i > 0):
                print()
            print (protein_translation[rna[i:i+3]], end="")
            if (protein_translation[rna[i:i+3]] == "-") :
                print("-")

intron_path = "introns.txt"
dna_path = "dna.txt"


introns = Util.parse_fasta(intron_path)
dna = "".join(Util.parse_fasta(dna_path))

exons = remove_introns(dna, introns)

rna = dna_to_rna(exons)

print_proteins(rna)
