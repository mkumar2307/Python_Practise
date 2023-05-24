'''
You are given N numbers on a circle described by an array A.
Find the maximum number of neighbouring pairs whose sums are even.
One element can belong to only one pair. Write a function: def solution(A)
'''

def neighbouring_pair(q):
    matches = []  # Initialize an empty list to store the indices of matching pairs

    # Iterate through the elements of the array except the last one
    for z in range(len(q) - 1):
        summ = int(q[z]) + int(q[(z + 1)])  # Calculate the sum of the current element and the next element

        # Check if the sum is even
        if (summ % 2) == 0:
            if z not in matches:  # Check if the current index is not already in the matches list
                matches.append((z + 1))  # Add the index of the next element to the matches list

    print(f"Number of matches: {len(matches)}")  # Print the number of matches found
    return len(matches)  # Return the count of matches


#input array
A = [4,2,5,8,7,3,7]
#call function
neighbouring_pair(A)