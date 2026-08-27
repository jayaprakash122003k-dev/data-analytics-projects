import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("sales_data.csv")

# Display data
print("Sales Data:")
print(df)

# Total sales and units
print("\nTotal Sales:", df["Sales"].sum())
print("Total Units:", df["Units"].sum())

# Sales by product
product_sales = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(product_sales)

# Sales by region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# Plot sales by product
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
