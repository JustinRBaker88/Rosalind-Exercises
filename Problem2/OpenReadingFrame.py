from BioUtil import Util

def get_open_reading_frames(reading_frames):
    orf = set()
    start_codons = []
    end_codons = []
    frame_index = 0
    for frames in reading_frames:
        start_codons.append([])
        end_codons.append([])
        codon_index = 0
        for codons in frames:
            if (Util.rna_codon_to_protein(codons) is "M"):
                start_codons[frame_index].append(codon_index)
            elif (Util.rna_codon_to_protein(codons) is "-"):
                end_codons[frame_index].append(codon_index)
            codon_index +=1
        frame_index += 1
    
    frame_index = 0
    for frames in start_codons:
        for indices in frames:
            ending_index =0
            for ends in end_codons[frame_index]:
                if ends > indices:
                    ending_index = ends
                    break
            start_index = indices
            temp_frame = []
            while (start_index < ending_index):
                temp_frame.append(Util.rna_codon_to_protein(reading_frames[frame_index][start_index]))
                #temp_frame.append(reading_frames[frame_index][start_index] + " ")
                start_index += 1
            if (len(temp_frame) > 0):
                temp = "".join(temp_frame)
                orf.add(temp)
        frame_index += 1
    return orf
    

def get_reading_frames(rna_string):
    reading_frames = []
    for i in range(0,6):
        reading_frames.append([])

    for index in range(0, len(rna_string)-3, 3):
        for f in range(0,3):
            reading_frames[f].append(rna[index+f:index+f+3])
            reading_frames[f+3].append(rna_compilment(rna[len(rna_string)-3-f-index:len(rna_string)-f-index])[::-1])
    return reading_frames         

def rna_compilment(rna_string):
    rna = []
    for basepairs in rna_string :
        if (basepairs == "A"):
            rna.append("U")
        elif(basepairs == "U"):
            rna.append("A")
        elif(basepairs == "C"):
            rna.append("G")
        else:
            rna.append("C")

            
    return "".join(rna)

def dna_compilment(dna_string):
    dna = []
    for basepairs in dna_string :
        if (basepairs == "A"):
            dna.append("T")
        elif(basepairs == "T"):
            dna.append("A")
        elif(basepairs == "C"):
            dna.append("G")
        else:
            dna.append("C")

            
    return "".join(dna)

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



def print_reading_frames(frames):
    for x in range(0,3):
        print("Frame ", x+1,  end=": ")
        for codons in frames[x]:
            print(codons, end=" ")
        print()
    for x in range(0,3):
        print("Frame", -1*(x+1),  end=": ")
        for codons in frames[x+3]:
            print(codons, end=" ")
        print()

intron_path = "introns.txt"
dna_path = "dna.txt"

introns = Util.parse_fasta(intron_path)
dna = "".join(Util.parse_fasta(dna_path))
exons = remove_introns(dna, introns)

print(exons)

rna = dna_to_rna(exons)

frames = get_reading_frames(rna)

print_reading_frames(frames)

orf = get_open_reading_frames(frames)
for frames in orf:
    print(frames)


