import numpy as np

points=[1,2,4,6,11,3]
pmf=[points[i]/sum(points) for i in range(len(points))]
c=0
n=len(points)

def random_sampler(pmf, no_of_samples):
    samples=[]
    sum=0
    cmf=[]
    for i in range(n):
        sum+=pmf[i]
        cmf.append(sum)
    for i in range(no_of_samples):
        r=np.random.uniform(0,1)
        for i in range (n):
            if r<cmf[i]:
                samples.append(i)
                break
    return samples

print(random_sampler(pmf, no_of_samples=4))

