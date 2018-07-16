import numpy as np

N=10000000

x = np.random.uniform(0,1,N)
y = np.random.uniform(0,1,N)

z = (x**2+y**2)**0.5
quarter = np.where(z<=1,1,0)
pii = sum(quarter)*4/float(N)
print(pii)





