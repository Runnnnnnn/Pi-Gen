import numpy as np

#number of simulation
N = 10000000

#generate a list of uniform numbers for x and y
x = np.random.uniform(0,1,N)
y = np.random.uniform(0,1,N)

#count the number of points within the quarter circle(d=1)
z = (x**2+y**2)**0.5
quarter = np.where(z<=1,1,0)

#calculate the value of pi
pii = sum(quarter)*4/float(N)
print(pii)





