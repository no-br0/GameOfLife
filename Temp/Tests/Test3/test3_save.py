import os

local_path = os.path.dirname(__file__)

path = local_path + "\data.txt"



order = []

def test0():
    print ("Test 0")
    
def test1():
    print ("Test 1")
    
order.append('test0()')
order.append('test1()')
order.append('test0()')


with open(path, 'w') as f:
    for i in order:
        f.write(str(i) + "\n")
