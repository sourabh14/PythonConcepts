import numpy as np

# NumPy (Numerical Python) is a powerful library for numerical computing in Python. It is especially valuable in data
# science, machine learning, and scientific computing because it provides efficient tools to work with large arrays
# and matrices, along with a wide array of mathematical functions to operate on these arrays.

# Key Features of NumPy
    # N-Dimensional Array:
        # The ndarray object, which is a multi-dimensional array, is the core of NumPy. Arrays are homogeneous,
        # meaning they contain elements of the same type, which allows for efficient memory usage and fast computations.
        # Arrays can be 1D (vectors), 2D (matrices), or higher-dimensional (tensors), and can be easily created, manipulated, and sliced.

    # Vectorized Operations:
        # NumPy allows for element-wise operations without the need for explicit loops, making computations much faster.
        # This is known as "vectorization" and allows for complex mathematical operations on entire arrays.
        # For example, you can add, subtract, or multiply two arrays directly, without using loops.

    # Broadcasting:
        # Broadcasting is a feature that allows NumPy to perform arithmetic operations on arrays of different shapes,
        # making it possible to perform operations between arrays without requiring them to have the same shape.
        # This is useful for scaling arrays, aligning arrays for operations, and more.

    # Mathematical Functions:
        # NumPy provides many mathematical functions to perform operations on arrays, including trigonometric, statistical, algebraic, and more.
        # You can compute functions like sine, cosine, exponential, logarithmic, maximum, minimum, etc., directly on arrays.

    # Linear Algebra:
        # It has a comprehensive set of linear algebra functions, including matrix operations (such as dot product, transpose,
        # and inverse) and solving linear equations, making it popular in fields like machine learning and scientific computing.

    # Random Number Generation:
        # NumPy has a submodule numpy.random for generating random numbers and arrays from various distributions, such as
        # uniform, normal, binomial, and others. This is often used in simulations and randomized algorithms.

    # Efficient Memory Usage and Performance:
        # NumPy is written in C, making it highly efficient in terms of memory and computation. Operations on NumPy arrays
        # are much faster than native Python data structures (e.g., lists) because of their fixed data types and contiguous memory storage.

    # Data Manipulation and Reshaping:
        # Arrays can be reshaped, transposed, stacked, split, and concatenated in flexible ways. This makes NumPy ideal
        # for preprocessing data, transforming datasets, and reshaping data for analysis.



# 1. Creating Arrays
# ------------------

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Creating arrays with specific shapes and values
zeros_array = np.zeros((2, 3))       # 2x3 array of zeros
ones_array = np.ones((3, 3))          # 3x3 array of ones
identity_matrix = np.eye(3)           # 3x3 identity matrix
print("Zeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)
print("Identity Matrix:\n", identity_matrix)

# Array of equally spaced values using arange and linspace
arange_array = np.arange(0, 10, 2)    # Array from 0 to 10 with step 2
linspace_array = np.linspace(0, 1, 5) # 5 values from 0 to 1
print("Arange Array:", arange_array)
print("Linspace Array:", linspace_array)

# 2. Basic Operations
# -------------------

# Array arithmetic
arr = np.array([10, 20, 30, 40])
print("Array:", arr)
print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)
print("Array / 10:", arr / 10)

# Element-wise operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)

# 3. Array Indexing and Slicing
# -----------------------------

arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)
print("First element:", arr[0])       # Accessing element at index 0
print("Last element:", arr[-1])       # Accessing last element
print("Slice from index 1 to 4:", arr[1:4])  # Slicing from index 1 to 3

# 2D Array slicing
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr2)
print("Element at (1,1):", arr2[1, 1])  # Element at 2nd row, 2nd column
print("First row:", arr2[0, :])         # First row
print("Last column:", arr2[:, -1])      # Last column

# 4. Array Properties and Reshaping
# ---------------------------------

# Checking shape, size, and data type
print("Shape of array:", arr2.shape)
print("Size of array:", arr2.size)
print("Data type:", arr2.dtype)

# Reshaping arrays
reshaped_array = arr2.reshape((1, 9))   # Reshape 3x3 to 1x9
print("Reshaped Array:\n", reshaped_array)

# 5. Statistical Functions
# ------------------------

arr = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Max value:", np.max(arr))
print("Index of Max value:", np.argmax(arr))

# 6. Linear Algebra Operations
# ----------------------------

# Dot product
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
dot_product = np.dot(arr1, arr2)
print("Dot product:", dot_product)

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix1, matrix2)
print("Matrix Product:\n", matrix_product)

# 7. Broadcasting
# ---------------

# Broadcasting allows you to perform operations on arrays of different shapes
arr = np.array([1, 2, 3])
scalar = 5
print("Array + Scalar (Broadcasting):", arr + scalar)

# 8. Random Numbers
# -----------------

# Generating random numbers
random_array = np.random.rand(3, 3)     # 3x3 array of random values between 0 and 1
normal_array = np.random.randn(3, 3)    # 3x3 array of normally distributed values
print("Random Array:\n", random_array)
print("Normal Distribution Array:\n", normal_array)
