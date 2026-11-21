
import numpy as np

# Create a random number generator with a fixed seed.
# Using the same seed produces the same random numbers every time.
rng = np.random.default_rng(seed=1)

# Generate a random float between 0 and 1 using uniform distribution.
random_uniform = rng.uniform()

# Print the generated random number.
print("Random number from uniform distribution:", random_uniform)
