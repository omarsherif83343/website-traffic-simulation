#project Simulation of a Website Traffic

import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

visitors_per_hour = 24

x = np.random.poisson(lam=20,size=visitors_per_hour)

max_visitors = np.max(x)
min_visitors = np.min(x)
avg_visitors = np.mean(x)

print('Max Visitors:- ',max_visitors)
print('Min Visitors:- ',min_visitors)
print('Average Visitors:- ',avg_visitors)


reshaped_visitors = x.reshape(6,4)

print('\nReshaped Visitors:')
print(reshaped_visitors)

midday_visitors = x[8:17]

print('\nMidday Visitors:')
print(midday_visitors)


shuffeled_visitors = x.copy()

print('\nShuffeled Visitors')

print(shuffeled_visitors)

np.random.shuffle(shuffeled_visitors)

registered_users = np.random.binomial(x,0.1)

print('\nRegistered Users Per Hour')
print(registered_users)

stay_times = np.random.normal(loc=5,scale=2,size=100)

mp.figure()
mp.hist(x)
mp.title('Visitors Per Hour Distribution')
mp.xlabel('Visitors')
mp.ylabel('Frequency')

mp.figure()
mp.hist(stay_times)
mp.title('Stay Time Distribution')
mp.xlabel('Minutes')
mp.ylabel('Frequency')
mp.show()









