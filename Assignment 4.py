"""1.Define a Python function progression(l) that takes a nonempty list of integers l and returns True if the integers in l form an arithmetic progression: that is, l is of the form [a,a+d,a+2d,…,a+kd]"""

def progression(mylist):
    if len(mylist)==1:
        return True
    else:
        k = mylist[1]-mylist[0]
        checklist =[]
        if k>0:
            for i in range(mylist[0],mylist[-1],k):
                checklist.append(i)
            checklist.append(checklist[-1]+k)
            return checklist == mylist
        if k<0:
            for i in range(mylist[-1],mylist[0],-k):
                checklist.append(i)
            checklist.append(checklist[-1]-k)
            checklist = checklist[::-1]
            return checklist == mylist
            
          
          
 
 """2. Write a Python function squareprime(l) that takes a nonempty list of integers and returns True if the elements of l alternate between perfect squares and prime numbers, and returns False otherwise. Note that the alternating sequence of squares and primes may begin with a square or with a prime."""
 
           
def squaretest(num):
    sqlist=[]
    i=1
    while i**2 <= num:
        sqlist.append(i**2) 
        i+=1
    return sqlist

def primecheck(num):
    primelist=[]
    for i in range(2,num + 1):
            for p in range(2,i):
                if (i % p) == 0:
                    break
            else:
                primelist.append(i)
    return primelist
  
  
  
def primesquare(l):
    if len(l)==1:
        primelist = primecheck(l[0])
        sqlist = squaretest(l[0])
        return (l[0] in primelist) or (l[0] in sqlist)
    else:
        ol=[]
        el=[]
        for i in range(0,len(l),2):
            ol.append(l[i])
        for p in range (1, len(l),2):
            el.append(l[p])
        primelist = primecheck(max(l))
        sqlist = squaretest (max(l))
        return((all(x in primelist for x in el)) == True and (all(y in sqlist for y in ol)) == True) or ((all(x in primelist for x in ol)) == True and (all(y in sqlist for y in el)) == True)
        
        
        
   """3. A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

1  2  3
4  5  6 
7  8  9
would be represented as [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

A horizonatal flip reflects each row. For instance, if we flip the previous matrix horizontally, we get

3  2  1
6  5  4 
9  8  7
which would be represented as [[3, 2, 1], [6, 5, 4], [9, 8, 7]].

A vertical flip reflects each column. For instance, if we flip the previous matrix that has already been flipped horizontally, we get

9  8  7
6  5  4 
3  2  1
which would be represented as [[9, 8, 7], [6, 5, 4], [3, 2, 1]].

Write a Python function matrixflip(m,d) that takes as input a two dimensional matrix m and a direction d, where d is either 'h' or 'v'. If d == 'h', the function should return the matrix flipped horizontally. If d == 'v', the function should retun the matrix flipped vertically. For any other value of d, the function should return m unchanged. In all cases, the argument m should remain undisturbed by the function.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix."""


def matrixflip(m, ch):
    if ch == 'h':
        newmat = []
        for i in range(0,len(m)):
            newmat.append(m[i][::-1])
        return newmat
        
    elif ch == 'v':
        return m[::-1]
    else:
        return m
