"""import numpy as np
"""
"""
a = np.array([10, 20, 30, 40, 50])

print("Array:", a)
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Size:", a.size)
print("Data type:", a.dtype)
print(a.shape)
"""
"""b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(b.shape)
print(b.ndim)
print(b.size)
print(b.dtype)
"""
"""
b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Array:", b)
print("Shape:", b.shape)
print("Dimensions:", b.ndim)
print("Size:", b.size)
print("Data type:", b.dtype)
"""
"""
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Original:", a)

print("Add 10:", a + 10)
print("Subtract 5:", a - 5)
print("Multiply by 2:", a * 2)
print("Divide by 2:", a / 2)
"""
"""
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print("a:", a)
print("b:", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
"""
"""
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Array:", a)

print("First element:", a[0])
print("Second element:", a[1])
print("Third element:", a[2])
print("Last element:", a[4])
print("Last:", a[-1])
print("Second last:", a[-2])
"""
"""
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Array:", a)

print("First 3:", a[0:3])
print("Middle:", a[1:4])
print("Last 2:", a[3:5])
print("From index 2:", a[2:])
print("Up to index 3:", a[:3])
"""
"""
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data)
print("10:", data[0, 0])
print("50:", data[1, 1])
print("90:", data[2, 2])
print("First row:", data[0, :])
print(data[0])
print("First column:", data[:, 0])
"""
"""
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Array:")
print(data)

print("Value at row 1, column 2:", data[1, 2])
print("Second row:", data[1])
print("Third column:", data[:, 2])
"""
"""
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

print("Original:")
print(a)

print("Original shape:", a.shape)

b = a.reshape(2, 3)

print("Reshaped:")
print(b)

print("New shape:", b.shape)
"""
"""
import numpy as np

marks = np.array([60, 70, 80, 90, 100])

print("Marks:", marks)

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard deviation:", np.std(marks))
"""
"""
import numpy as np

x = np.random.rand()

print("Random number:", x)
"""
"""
import numpy as np
numbers = np.random.rand(5)

print(numbers)
"""
#syntax is = np.random.randint(start, end, size)
"""
import numpy as np
numbers = np.random.randint(1, 101, 5)

print(numbers)
"""
"""
import numpy as np

np.random.seed(42)

numbers = np.random.randint(1, 101, 5)

print(numbers)
"""
"""
import numpy as np

a = np.array([10, 25, 50, 65, 80, 35, 90])

print(a)
print(a > 50)
print(a[a > 50])
"""
"""
import numpy as np

a = np.array([10, 25, 50, 65, 80, 35, 90])

print("Original:", a)

print("Greater than 50:", a[a > 50])
print("Less than 50:", a[a < 50])
print("Greater than or equal to 50:", a[a >= 50])
print("Equal to 50:", a[a == 50])
"""
"""
import numpy as np

marks = np.array([35, 45, 60, 75, 90])

result = np.where(marks >= 50, "Pass", "Fail")

print(result)
#np.where(condition, value_if_true, value_if_false)
"""
"""
#If the price is ≥ 500, give a 10% discount. Otherwise, keep the original price.
#EXAMPLE 1
import numpy as np
prices = np.array([100, 250, 500, 750, 1000])

result = np.where(prices >= 500, prices * 0.9, prices)

print(result)
"""
"""
import numpy as np

scores = np.array([30, 55, 72, 40, 90, 65])

result = np.where(scores >= 50, "Pass", "Fail")

print("Scores:", scores)
print("Result:", result)
"""

