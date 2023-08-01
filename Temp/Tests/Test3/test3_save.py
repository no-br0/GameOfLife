import os
from test3_func import test0, test1

local_path = os.path.dirname(__file__)

path = local_path + "\data.txt"



order = []

#output = "Hello World"
#output2 = "Second Output"
    
order.append('test0(output)')
order.append('test1()')
order.append('test0(output2)')


with open(path, 'w') as f:
    for i in order:
        f.write(str(i) + "\n")
