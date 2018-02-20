from BioUtil import Util
import numpy

def global_allignment_score(strand1, strand2):
    n = len(strand1)
    m = len(strand2)
    
    scoreMatrix = generateScoreMatrix(strand1, strand2)
    
    return int(scoreMatrix[n][m])

def generateScoreMatrix(strand1, strand2):
    n = len(strand1) +1
    m = len(strand2) +1
    scoreMatrix = numpy.zeros((n, m))
    
    for i in range (0, n):
        scoreMatrix[i][0] = i * -5
    for i in range (0, m):
        scoreMatrix[0][i] = i * -5
    
    for i in range(1, n):
        for j in range(1, m):
            above = -5
            left = -5
            diag = Util.get_blosum62_score(strand1[i-1], strand2[j-1])
            
            scoreMatrix[i][j] = max(above +scoreMatrix[i-1][j], left + scoreMatrix[i][j-1], diag + scoreMatrix[i-1][j-1])

    
    return scoreMatrix

path = "./data.txt"
data = Util.parse_fasta(path)

print(global_allignment_score(data[0], data[1]))
