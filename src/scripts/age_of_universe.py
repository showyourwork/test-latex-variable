
import paths
import numpy as np

# Compute the age of the universe
np.random.seed(42)
age = np.random.normal(14.0, 1.0)

# Write it to disk
with open(paths.output / "age_of_universe.txt", "w") as f:
    f.write(f"{age:.3f}")

