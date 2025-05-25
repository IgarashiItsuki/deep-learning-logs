import numpy as np

"""
パーセプトロンを用いることで、AND,NAND,ORなどの論理回路が実現できる
"""
def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(x*w)+b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(x*w)+b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(x*w)+b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1
    
"""
単層のパーセプトロンでは、XORは表せない。2層なら可能
"""
def XOR(x1,x2):
    tmp=AND(NAND(x1, x2),OR(x1, x2))
    if tmp>0:
        print(1)
        return 1
    elif tmp<=0:
        print(0)
        return 0

XOR(0,0)
XOR(0,1)
XOR(1,0)
XOR(1,1)    
    