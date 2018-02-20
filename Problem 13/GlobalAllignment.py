from BioUtil import Util


path = "./data.txt"
data = Util.parse_fasta(path)

print(data)

print (Util.get_blosum62_score('F', 'D'))