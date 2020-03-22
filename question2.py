#do not import any libraries for this question
"""
Write a function that takes a list of integers as input and returns the sum of the even numbers in the list
minus the sum of the odd numbers in the list. The list may contain zeros and negative numbers. For example,
f([0, -4, 2, -3, 6, -1, 8, 6]) should return 22.

You can test your function by running "python question2.py" Note: Do not tailor your function
to the specific test case given. It is there to help you test whether your function works or not,
but the idea is that it should work properly for any given input.
"""

def f(l):
    ##########YOUR CODE HERE##########
    L1 = [0,-4,2,-3,6,-1,8,6]
L3 = []
L4 = []
for x in L1:
    if x%2 == 0:
        L3.append(x)
    else:
        L4.append(x)
def f(x):
    return sum(L3)-sum(L4)

print(f(x))
    ###########END CODE###############

#Do not edit the code below
if __name__=='__main__':
    y = f([0, -4, 2, -3, 6, -1, 8, 6])
    if y == 22:
        print('Test passed')
    else:
        print('Test failed, y = {} when it should have been 22'.format(str(y)))
