import random
import numpy as np
import matplotlib.pyplot as plt
# compute for j Xj and then add 1/10 of it to array value and plot
n = 10000
mk=0
X = []
Y = []
Z = []
for j in range (0,n):
    Xj = random.choice([-1,1])
    Xj = Xj
    X.append(mk/100)
    mk +=Xj 
    
mk=0
for j in range (0,n):
    Xj = random.choice([-1,1])
    Xj = Xj
    Y.append(mk/100)
    mk +=Xj 
mk=0
for j in range (0,n):
    Xj = random.choice([-1,1])
    Xj = Xj
    Z.append(mk/100)
    mk +=Xj
t = np.linspace(0, 1, n)


plt.plot(t,X)
plt.plot(t,Y)
plt.plot(t,Z)
plt.xlabel("Step")
plt.ylabel("M_k")
plt.title("Random Walk Simulation")

plt.grid(True)

plt.show()