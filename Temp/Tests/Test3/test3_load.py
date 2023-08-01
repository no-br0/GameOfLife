import os
from test3_func import test0, test1

local_path = os.path.dirname(__file__)

path = local_path + "\data.txt"

order = []

output = "Hello World"
output2 = "Second Output"

with open(path, 'r') as f:
    for i in f.readlines():
        order.append(i)
        #print(i)



#print (order[0])
for i in order:
    exec(i)
#eval(order[0])