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

# Reads through first string and takes all substrings (from longest to shortest)
# in this string and checks if it is contained in all other strings.
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                test_substring = data[0][i:i + j]
                if j > len(substr) and is_common_substring(test_substring, data):
                    substr = test_substring
    return substr

def is_common_substring(search_substring, all_strings):
    if len(search_substring) < 1:
        return False
    for i in range(len(all_strings)):
        if search_substring not in all_strings[i]:
            return False
    return True

path = "./data.txt"

data = parse_fasta(path)
print (long_substr(data))