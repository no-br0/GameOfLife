from dataclasses import dataclass
#NOTE: in order to make a condition with only 1 value as a requirement the format (n,) is essential
# this is due to a tuple with a single value needing the comma to be recognised as a tuple
@dataclass
class transition:
    curstate:int
    nextstate:int
    condition:tuple

@dataclass
class neigh_transition(transition):
    num_neigh:int