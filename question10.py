from datetime import datetime, timedelta
#do not imnport any other libraries
"""
Write a function that takes 2 strings s1 and s2 as inputs. These strings will represent times of the day and will be written in the format
HH:MM:SS. Your function should return the number of seconds between these 2 times. You may assume s2 always represents a later time than s1.
There are a number of ways to do this problem, but you will find making use of the datetime.datetime and datetime.timedelta modules will make
things easiest. For example, f('08:59:59','10:24:31') should return 5072.

You can test your function by running "python question10.py" Note: Do not tailor your function
to the specific test case given. It is there to help you test whether your function works or not,
but the idea is that it should work properly for any given input.
"""

from datetime import datetime
s1 = "22:31:14"
s2 = "23:12:40"

def f(s1,s2):
    do1 = datetime.strptime(s1, "%H:%M:%S")
    do2 = datetime.strptime(s2, "%H:%M:%S")
    do3 = do2-do1
    return do3.total_seconds()
print(f(s1,s2))
    ###########END CODE###############

#Do not edit the code below
if __name__=='__main__':
    y = f('08:59:59','10:24:31')
    if y == 5072:
        print('Test passed')
    else:
        print('Test failed, y = {} when it should have been 5072'.format(str(y)))
