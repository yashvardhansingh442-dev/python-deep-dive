import numpy as np          

#The numpy.random.seed() function initializes NumPy's pseudo-random number generator with a specific 
#starting value so that your code produces predictable, repeatable random numbers every time it runs

# Generate random numbers from a uniform distribution
random_uniform = np.random.default_rng(seed=1).uniform() #this will generate a random float between 0 and 1

print("Random number from uniform distribution: ", random_uniform)