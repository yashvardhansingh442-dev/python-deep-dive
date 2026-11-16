import numpy as np

# Generate random integers
# seed is used to initialize the random number generator, so that the same random numbers are generated each time the code is run.

rng = np.random.default_rng()  # Create a random number generator
print("this is the random number generator: ", rng.integers(low=1, high=6))
# Generate random numbers
random_numbers = np.random.randint(
    1, 100, size=(5, 1)
)  # this will generate 5 random integers between 1 and 100
print("Random Numbers: ", random_numbers)

# Generate random floats
random_floats = np.random.rand(5)  # this will generate 5 random floats between 0 and 1
print("Random Floats: ", random_floats)
