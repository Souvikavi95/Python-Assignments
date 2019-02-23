"""1. A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.

Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise."""

def valley(lst):
    if len(lst)<2:
        return False
  
    else:
        p = lst.index(min(lst))
        for i in range (0,p):
            x = (lst[i] > lst[i+1])
                
        for q in range (p,len(lst)-1):
            y = (lst[q]< lst[q+1])
               
        return (x==y)
        
        
        
        
 """2. A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

  1  2  3
  4  5  6 
would be represented as [[1, 2, 3], [4, 5, 6]].

The transpose of a matrix makes each row into a column. For instance, the transpose of the matrix above is

  1  4  
  2  5
  3  6
Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the transpose of the matrix using the same representation.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix."""

def transpose(lst):
    newlist = []
    i=0
    if len(lst)<3:
        while i <= len(lst):
            j = 0
            column = []
            while j < len(lst):
                column.append(lst[j][i])
                j+=1
            newlist.append(column)
            i += 1
        return newlist
    else:
        while i <len(lst):
            j = 0
            column = []
            while j < len(lst):
                column.append(lst[j][i])
                j+=1
            newlist.append(column)
            i += 1
        return newlist
