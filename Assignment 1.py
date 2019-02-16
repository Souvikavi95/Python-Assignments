"""1.Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n."""

solution :

def intreverse(num):
    
    strg = str(num)
    return int(strg[::-1])
  

"""2.Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. 
 Your function should return True if s has matched brackets and False if it does not.
  Hint: Keep track of the nesting depth of brackets. Initially the depth is 0. 
  The depth increases with each opening bracket and decreases with each closing bracket. 
  What are the constraints on the value of the nesting depth for all brackets to be matched?"""

solution :

def matched(s):
    
    j = 0
    for c in s:
        if c == ')':
            j -= 1
            if j < 0:
                return False
        elif c == '(':
            j += 1
    return j == 0

"""3.Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l."""

def sumprimes(l):
    result = 0   
    for num in l:
        if num>0:
            for i in range(2,num):
                if num%i == 0:
                    break
                
            else:
                result += num
    return (result)
     
     
     


