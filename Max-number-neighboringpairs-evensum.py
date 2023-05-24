'''
You are given N numbers on a circle described by an array A.
Find the maximum number of neighbouring pairs whose sums are even.
One element can belong to only one pair. Write a function: def solution(A)
'''

def neighbouring_pair(q):
    matches = []
    for z in range(len(q) - 1):
        summ = int(q[z]) + int(q[(z + 1)])
        if (summ % 2) == 0:
            if z not in matches:
                matches.append((z + 1))
    print(f"Number of matches: {len(matches)}")
    return len(matches)

#input array
A = [4,2,5,8,7,3,7]
#call function
neighbouring_pair(A)