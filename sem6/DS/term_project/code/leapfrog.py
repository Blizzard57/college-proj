# It was given that any programming language would work and 
# so I chose python for Monte Carlo Simulation
import numpy as np
import ray

ray.init()

@ray.remote
def piEst(N):
    val = 0
    for  i in range(N):
        x = np.random.uniform()
        y =  np.random.uniform()
        if x**2 + y**2 < 1:
            val += 1
    
    return val/N

# Simulations per processor
N = 1000 

resultIds = []
for i in range(proc):
    resultIds.append(piEst.remote(N))

Rk = ray.get(resultIds)

print("The value of pi is : "mean(Rk))