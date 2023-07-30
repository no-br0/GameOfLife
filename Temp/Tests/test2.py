l = []

def test0():
    print("Test 0")
    
def test1():
    print("Test 1")

print("append start")
l.append(test0)
l.append(test1)
l.append(test0)
print("append end")

for i in l:
    i()