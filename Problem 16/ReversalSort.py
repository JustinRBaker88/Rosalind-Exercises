import copy
import random

def reversalSort(source, target):
    s = copy.deepcopy(source)
    t = copy.deepcopy(target)
    swaps = []
    convert_to_identity(s, t)
    curr_breakpoints = calc_breakpoints(s)
    while curr_breakpoints > 0 :
        des = descending_indices(s)
        asc = ascending_indices(s)
        
        #removing already sorted ascended sequences
        i = 0
        while (i < len(asc)):
            for values in asc[i]:
                if (values == 0):
                    asc.pop(i)
                    i -= 1
                    break
            i += 1   
        
        starts = []
        ends = []
        for values in des:
            starts.append(values[0])
            starts.append(values[1])
            ends.append(values[0])
            ends.append(values[1])
        for i in  range(0, len(asc)):
            starts.append(asc[i][0])
            starts.append(asc[i][1])
            ends.append(asc[i][1])
            ends.append(asc[i][0])
        
        ones = []
        twos = []
        if len(des) > 0:
            bp = curr_breakpoints
            optimal_found = False
            for i in range(1, len(s)):
                for j in range(1, len(s) + 1):
                    if ( i >= j):
                        continue

                    rev = reverse(s, i, j)
                    bp = calc_breakpoints(rev)
                    if (bp == curr_breakpoints - 2):
                        twos.append((i,j))
                    elif (bp == curr_breakpoints - 1):
                            ones.append((i,j))
            
            if (len(twos) > 0):
                r = random.randint(0, len(twos) -1)
                s = reverse(s, twos[r][0], twos[r][1])
                curr_breakpoints = calc_breakpoints(s)
                swaps.append((twos[r][0], twos[r][1]))
            elif(len(ones) > 0):
                r = random.randint(0, len(ones) -1)
                s = reverse(s, ones[r][0], ones[r][1])
                curr_breakpoints = calc_breakpoints(s)
                swaps.append((ones[r][0], ones[r][1]))
            else:
                s = reverse(s, ones[0][0], ones[0][1])
                curr_breakpoints = calc_breakpoints(s)
                swaps.append((ones[0][0], ones[0][1]))
            
        else:
            swaps.append((asc[0][0], asc[0][1]))
            s = reverse(s, asc[0][0], asc[0][1])

    return (len(swaps), swaps)

def convert_to_identity(pi, gamma):
    conversion = {}
    index = 1
    for keys in gamma:
        conversion[keys] = index
        index += 1
    index = 0
    for keys in pi:
        gamma[index] = index + 1
        pi[index] = conversion[keys]
        index += 1

def calc_breakpoints(sequence):
    if (len(sequence) <= 2):
        return 0
    prev = 0
    current = sequence[0]
    bp = 0
    for i in range(0, len(sequence)):
        current = sequence[i]
        if (prev + 1 != current and prev -1 != current):
            bp += 1
        prev = current
    if (current + 1 != len(sequence) + 1):
        bp += 1
    return bp

def ascending_indices(sequence):
    asc = []
    start = 0
    end = 0
    
    curr_ascending = False
    prev_ascending = True
    curr_descending = False
    prev_descending = False
    prev = 0
    curr = sequence[0]
    next = sequence[1]
    
    if (sequence[0] == 1):
        curr_ascending = True
        end = 1
    else:
        curr_descending = True

        

    i = 0
    while (i < len(sequence)):
        if (i == len(sequence) - 1):
            prev = curr
            curr = next
            next = len(sequence) + 1
        elif(i > 0):
            prev = curr
            curr = next
            next = sequence[i+1]

        if (prev + 1 == curr):
            # continuing ascending sequence
            curr_ascending = True
            curr_descending = False
            end += 1
        elif (prev - 1 == curr):
            # continuing descending sequence
            curr_ascending = False
            curr_descending = True
            start = i + 1
            end += 1
        else:
            if (curr + 1 == next):
                #new ascending sequence
                if (prev_ascending):
                    asc.append((start,end))
                curr_ascending = True
                curr_descending = False
                start = i + 1
                end = i + 1
            else:
                # new descending sequence
                if (prev_ascending):
                    asc.append((start,end)) 
                start = i + 1
                end = start
                curr_ascending = False
                curr_descending = True
        prev_ascending = curr_ascending
        prev_descending = curr_descending
        i += 1
            

    return asc     

def descending_indices(sequence):
    des = []
    start = 1
    end = 1
    
    curr_ascending = False
    prev_ascending = True
    curr_descending = False
    prev_descending = False
    prev = 0
    curr = sequence[0]
    next = sequence[1]
        
    if (sequence[0] == 1):
        curr_ascending = True
    else:
        curr_descending = True

        

    i = 0
    while (i < len(sequence)):
        if (i == len(sequence) - 1):
            prev = curr
            curr = next
            next = len(sequence) + 1
        elif(i > 0):
            prev = curr
            curr = next
            next = sequence[i+1]

        if (prev + 1 == curr):
            # continuing ascending sequence
            curr_ascending = True
            curr_descending = False
            start += 1
            end += 1
        elif (prev - 1 == curr):
            # continuing descending sequence
            curr_ascending = False
            curr_descending = True
            end += 1
        else:
            if (curr + 1 == next):
                #new ascending sequence
                if (prev_descending):
                    des.append((start,end))
                curr_ascending = True
                curr_descending = False
                start = i + 1
                end = i + 1
            else:
                # new descending sequence
                if (prev_descending):
                    des.append((start,end)) 
                start = i + 1
                end = start
                curr_ascending = False
                curr_descending = True
        prev_ascending = curr_ascending
        prev_descending = curr_descending
        i += 1
            
    if (prev_descending):
        end += 1
        des.append((start,end))
        
    return des        
        
def reverse(sequence, start, end):
    if (start == end):
        print(start)
        print(end)
        print("can't reverse")
        return sequence
    
    start -= 1
    reversed = [] 
    sub = sequence[start:end][::-1]
    for i in range (0, start):
        reversed.append(sequence[i])
    for values in sub:
        reversed.append(values)
    for i in range(end, len(sequence)):
        reversed.append(sequence[i])
    return reversed


pi = [8, 7, 4, 2, 3, 5, 1, 6, 10, 9]
gamma = [5, 2, 7, 3, 6, 8, 9, 1, 10, 4]

answer = reversalSort(pi, gamma)
smallest = answer[0]
for i in range(100):
    temp = reversalSort(pi, gamma)
    if (temp[0] < smallest):
        answer = temp
        smallest = temp[0]
        
        
print(pi)
rev = copy.deepcopy(pi)
for values in answer[1]:
    rev = reverse(rev,values[0], values[1])
    print(rev, " p = R(p, ", values[0], " ", values[1],")")

print()
print(smallest)
for values in answer[1]:
    print(values[0], values[1])





