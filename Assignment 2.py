"""1.A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.

Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned as primes and False otherwise. (If m is not positive, your function should return False.)"""
solution :

def primepartition(m):
    primelist=[]
    if m<0:
        return False
    else:
        for i in range(2,m + 1):
            for p in range(2,i):
                if (i % p) == 0:
                    break
            else:
                primelist.append(i)
            
        for x in primelist:
            y= m-x
            if y in primelist:
                return True
        return False
        
        
 """2.Write a function nestingdepth(s) that takes as input a string s and computes the maximum nesting depth of brackets if s has properly nested brackets. If the string is not properly matched, your function should return -1."""

solution :
 
def nestingdepth(s): 
    new_max = 0
    max = 0 
    for i in range(len(s)): 
        if s[i] in '([{': 
            new_max += 1
  
            if new_max > max: 
                max = new_max 
        elif s[i] in ')]}': 
            if new_max > 0: 
                new_max -= 1
            else: 
                return -1
    if new_max != 0: 
        return -1
  
    return max



  """3.A list rotation consists of taking the first element and moving it to the end. For instance, if we rotate the list [1,2,3,4,5], we get [2,3,4,5,1]. If we rotate it again, we get [3,4,5,1,2]."""
solution :

def rotatelist(l, k):
    if k<0:
        return l
    else:
        return l[k % len(l):] + l[:k % len(l)] 
