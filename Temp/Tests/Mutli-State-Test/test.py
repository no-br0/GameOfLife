import numpy as np
        

data = np.zeros([5,5,2],dtype=int)

output = data.take(range(1-1, 1+2), mode='wrap', axis=0).take(range(1-1,1+2), mode='wrap', axis=1)
for i in output:
    print(i)
#print(data[0][0])