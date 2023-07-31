import os

local_path = os.path.dirname(__file__)

path = local_path + "\data.txt"

order = []

def test0():
    print ("Test 0")
    
def test1():
    print ("Test 1")
    

with open(path, 'r') as f:
    for i in f.readlines():
        order.append(i)
        #print(i)



#print (order[0])
for i in order:
    exec(i)
#eval(order[0])