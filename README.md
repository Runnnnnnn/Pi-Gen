import numpy as np
x = np.random.uniform(0,1,10000000)
y = np.random.uniform(0,1,10000000)

z = (x**2+y**2)**0.5
quarter_fan = np.where(z<=1,1,0)
pii = sum(quarter_fan)*4/float(len(x))
print(pii)
