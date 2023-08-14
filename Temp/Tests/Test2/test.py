#Note Both methods work properly

l = []
l2 = []

def test0():
    print("Test 0")
    
def test1():
    print("Test 1")

print("append start")
l.append(test0)
l.append(test1)
l.append(test0)
l2.append(lambda: test0())
l2.append(lambda: test0())
l2.append(lambda: test0())
print("append end")

for i in l:
    i()
    
for i in l2:
    i()
    
print(11%10)