#Do not import any libraries for this question
"""
Write a function that takes a list of numbers as input and returns the median of the list.

You can test your function by running "python question4.py" Note: Do not tailor your function
to the specific test case given. It is there to help you test whether your function works or not,
but the idea is that it should work properly for any given input.
"""
def f(l):
    a = sorted(l)
    b = len(a)
    if b%2 == 0:
            return print((a[b//2]+a[b//2-1])/2)
    else:
            return (a[b//2])

l = [5,21,14,9,13]
print(f(l))
    ###########END CODE###############

#Do not edit the code below
if __name__=='__main__':
    y = f([1,2,5,8,2,5,8,2,5,2,7,5,2,4,43])
    if y == 5:
        print('Test passed')
    else:
        print('Test failed, y = {} when it should have been 5'.format(str(y)))
