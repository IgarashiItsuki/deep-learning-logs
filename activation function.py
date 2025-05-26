import numpy as np
import matplotlib.pylab as plt

def step_function_1(x):
    #ただこれだとNumpy配列を扱えない。スカラー比較になる。
    if x> 0:
        return 1
    else:
        return 0
    
def step_function_2(x):
    y=x>0
    return y.astype(np.int_)
#np.array(y, dtype=元の型).astype(np.int)
#上のやつの略で、ブール値をスカラ値に変換する。

#
def step_function(x):
     return np.array(x>0,dtype=np.int_)

X=np.arange(-5.0,5.0,0.1)
Y=step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # 図で描画するy軸の範囲を指定
plt.show()