from BioUtil import Util

# Reads through first string and takes all substrings (from longest to shortest)
# in this string and checks if it is contained in all other strings.
def long_substr(data):
    longest = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                test_substring = data[0][i:i + j]
                if len(test_substring) > len(longest) and Util.is_common_substring(test_substring, data):
                    longest = test_substring
    return longest



path = "./data.txt"

data = Util.parse_fasta(path)
print (long_substr(data))