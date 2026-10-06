#Mean
"""
import numpy as np

data = np.array([10, 20, 30, 40, 50])

mean = np.mean(data)

print("Mean:", mean)
"""
#Example
"""import numpy as np 
data = np.array([15, 25, 35, 45, 55])
mean = np.mean(data)
print("Mean:", mean)
"""
#Median
"""import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Median:", np.median(data))

data = np.array([10, 20, 30, 40])

print("Median:", np.median(data))
"""
#Mode
"""import statistics

data = [10, 20, 20, 30, 40]

print("Mode:", statistics.mode(data))
"""
#Range
"""import numpy as np

data = np.array([10, 20, 30, 40, 50])

range_value = np.max(data) - np.min(data)

print("Range:", range_value)
"""
#Variance
"""import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Variance:", np.var(data))
print("Standard deviation:", np.std(data))
"""
#Example
"""import numpy as np

data = np.array([5, 10, 15, 20, 25])

print("Variance:", np.var(data))
"""

#Full Main Example
"""import numpy as np

numbers = np.array([2, 4, 6, 8, 10])

print("Mean:", np.mean(numbers))
print("Variance:", np.var(numbers))
print("Standard deviation:", np.std(numbers))
"""

