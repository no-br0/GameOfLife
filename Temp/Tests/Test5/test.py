from dataclasses import dataclass

@dataclass
class rep:
    value:int
    condition:tuple
    
    
out = rep(1,(3,2,))
print(out.condition)
if 3 in out.condition:
    print("it worked")