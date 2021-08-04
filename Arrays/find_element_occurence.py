
# Given an array arr[] and size of array is n and one another key x, and give you a segment size k.
# The task is to find that the key x present in every segment of size k in arr[].

                    # python solution

def element_occurence(arr,x,k,n):
    i = 0
    while i < n :
        j = 0 
        while j < k:
            if arr[i+j]==x:
                break
            j = j+1
        if j == k :
            return False

        i = i + k
    if i == n :
        return True
      
# Check in last segment if n is not multiple of k.

    j = i - k
    while j < n:
        if arr[j]== x:
            break
        j = j + 1
    if j == n :
        return True

arr = [1,3,4,3,6,4,7,8,3,10,1,3]
x = 3
k = 3
n = len(arr)

if(element_occurence(arr,x,k,n)):
    print("yes element is present")
else :
    print("element not present")
