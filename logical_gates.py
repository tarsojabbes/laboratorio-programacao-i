from p1 import Array

a = Array()
print(a)
def or_gate(a, b):
    if a == 0 and b == 0:
        return 0
    return 1

def and_gate(a,b):
    if a == 1 and b == 1:
        return 1
    return 0

def not_gate(a):
    return not a

def nand_gate(a,b):
    return not and_gate(a,b)

def nor_gate(a,b):
    return not or_gate(a,b)

