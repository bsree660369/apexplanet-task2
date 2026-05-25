import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load Dataset
df = pd.read_csv("sales_data.csv")

# Show First 5 Rows
print("FIRST 5 ROWS")
print(df.head())

# Show Dataset Information
print("\nDATASET INFO")
print(df.info())

# Show Statistics
print("\nSTATISTICS")
print(df.describe())

# Create Histogram Graph
df['"1958"'].hist()

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()

# Create SQL Database
conn = sqlite3.connect("sales.db")

# Store Dataset into SQL Table
df.to_sql("sales", conn, if_exists="replace", index=False)

# SQL Query
query = """
SELECT SUM('"1958"') as TotalSales
FROM sales;
"""

# Execute Query
result = pd.read_sql(query, conn)

# Print SQL Output
print("\nSQL OUTPUT")
print(result)