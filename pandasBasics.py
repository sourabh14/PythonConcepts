import pandas as pd

# Intro
    # Pandas is a powerful open-source data analysis and data manipulation library for Python. It is widely used in
    # data science, finance, statistics, and other fields for working with structured data, such as tabular data,
    # time series, and matrix data. Built on top of NumPy, pandas provides high-level data structures and tools that make
    # data analysis fast and efficient.

# Key Components of Pandas
    # Series:
        # A Series is a one-dimensional labeled array that can hold any data type (integers, strings, floats, etc.).
        # Think of it as a single column of data with an index.
        # It is commonly used for handling time series data, where each value has an associated timestamp or label.

    # DataFrame:
        # A DataFrame is a two-dimensional labeled data structure, similar to a table in SQL or Excel. It consists of
        # rows and columns, with each column typically representing a feature (attribute) of the data.
        # DataFrames are the most commonly used data structure in pandas for data analysis tasks.

# Key Features of Pandas
    # Data Cleaning:
        # Pandas has many tools for handling messy data. You can identify and fill missing values, drop or fill NaN
        # values, and handle duplicates, which is essential in real-world data preprocessing.

    # Data Transformation:
        # Provides capabilities for filtering, merging, grouping, and reshaping data. You can apply various
        # transformations to rows and columns, allowing you to manipulate and reformat data according to analysis needs.

    # Aggregation and Grouping:
        # Grouping allows you to split data into groups, apply specific operations to each group, and combine results.
        # This is useful for summarizing data, such as calculating averages or other statistics by group.

    # Indexing and Selection:
        # Pandas supports multiple ways to access and modify data, including label-based indexing (.loc) and position-based
        # indexing (.iloc). You can also select specific rows, columns, or values to analyze or modify data in a DataFrame.

    # Handling Time Series Data:
        # Pandas has robust time series functionality for handling date and time data. You can resample time-based data,
        # calculate rolling statistics, and handle data with different time frequencies, which is valuable in fields like
        # finance and economics.

    # High-Performance Operations:
        # Because it is built on NumPy, pandas is highly efficient, especially with large datasets. It uses vectorized
        # operations and optimizations that allow for fast data manipulation.

    # Data Import and Export:
        # Pandas supports importing and exporting data from multiple file formats, including CSV, Excel, SQL databases,
        # JSON, and more. This flexibility makes it easy to work with diverse data sources and share results.

    # Visualization Integration:
        # While pandas is not primarily a visualization library, it provides basic support for plotting data using
        # matplotlib for quick visual analysis. You can generate line plots, bar plots, histograms, and more directly from DataFrames.



# 1. Series - 1D labeled array
# ----------------------------

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print("Series:\n", series)

# Accessing elements
print("Element at index 'c':", series['c'])
print("Series values:", series.values)
print("Series index:", series.index)

# 2. DataFrame - 2D labeled data structure
# ----------------------------------------

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Creating a DataFrame from a CSV file
# (Assuming there is a file 'sample_data.csv' in the same directory)
df2 = pd.read_csv('sample_data.csv')
print("\nData from CSV file:\n", df2)

# 3. Basic Data Exploration
# -------------------------

print("\nDataFrame Info:\n")
print(df.info())                 # Summary of the DataFrame
print("\nFirst 2 rows:\n", df.head(2)) # Display first n rows
print("\nStatistics:\n", df.describe()) # Summary statistics for numeric columns

# 4. Indexing and Slicing
# -----------------------

# Selecting a column
print("\nAge column:\n", df['Age'])

# Selecting multiple columns
print("\nName and City columns:\n", df[['Name', 'City']])

# Selecting rows by label (loc) and by index position (iloc)
print("\nRow with label 2:\n", df.loc[2])
print("\nRow at position 1:\n", df.iloc[1])

# Selecting a subset of rows and columns
print("\nSubset of rows and columns:\n", df.loc[1:3, ['Name', 'Age']])

# 5. Data Manipulation
# --------------------

# Adding a new column
df['Salary'] = [70000, 80000, 65000, 120000]
print("\nDataFrame with new Salary column:\n", df)

# Updating values
df.loc[0, 'Age'] = 25
print("\nDataFrame after updating Age:\n", df)

# Deleting a column
df = df.drop('Salary', axis=1)
print("\nDataFrame after deleting Salary column:\n", df)

# Filtering data
adults_df = df[df['Age'] >= 25]
print("\nFiltered DataFrame (Age >= 25):\n", adults_df)

# 6. Handling Missing Data
# ------------------------

# Creating a DataFrame with missing values
data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [24, None, 22, 32],
    'City': ['New York', 'San Francisco', None, 'Chicago']
}
df_nan = pd.DataFrame(data_with_nan)
print("\nDataFrame with NaN values:\n", df_nan)

# Checking for missing values
print("\nMissing values in DataFrame:\n", df_nan.isnull())

# Filling missing values
df_nan_filled = df_nan.fillna({'Name': 'Unknown', 'Age': df_nan['Age'].mean(), 'City': 'Unknown'})
print("\nDataFrame with NaN values filled:\n", df_nan_filled)

# Dropping rows with any missing values
df_nan_dropped = df_nan.dropna()
print("\nDataFrame with NaN values dropped:\n", df_nan_dropped)

# 7. Aggregation and Grouping
# ---------------------------

# Group by City and calculate the mean age
df_grouped = df.groupby('City')['Age'].mean()
print("\nAverage Age by City:\n", df_grouped)

# Aggregating multiple functions
agg_result = df.groupby('City').agg({'Age': ['mean', 'max', 'min']})
print("\nAggregated Statistics:\n", agg_result)

# 8. Sorting and Ordering
# -----------------------

# Sorting by Age in descending order
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age (descending):\n", sorted_df)

# Sorting by multiple columns
sorted_df_multi = df.sort_values(by=['City', 'Age'])
print("\nDataFrame sorted by City and Age:\n", sorted_df_multi)

# 9. Merging and Joining DataFrames
# ---------------------------------

# Creating two DataFrames to merge
data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
data2 = {'ID': [1, 2, 3], 'Score': [85, 90, 88]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merging DataFrames on a common column
merged_df = pd.merge(df1, df2, on='ID')
print("\nMerged DataFrame:\n", merged_df)

# 10. Exporting Data
# ------------------

# Saving the DataFrame to a CSV file
# df.to_csv('output_data.csv', index=False)
# print("\nDataFrame saved to 'output_data.csv'")
