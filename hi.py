import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('orders.csv')

# Set the style of seaborn for better aesthetics
sns.set(style="whitegrid")

# Bar Plot: Total amount per Customer
plt.figure(figsize=(10, 6))
df.groupby('Customer name')['Total'].sum().sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Total Order Amount per Customer')
plt.xlabel('Customer Name')
plt.ylabel('Total Order Amount')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Histogram: Distribution of Order Quantity
plt.figure(figsize=(10, 6))
sns.histplot(df['Quantity'], kde=True, bins=15, color='teal')
plt.title('Distribution of Order Quantities')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter Plot: Quantity vs. Total Order Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Quantity', y='Total', hue='Order Type', palette='deep')
plt.title('Quantity vs. Total Order Amount')
plt.xlabel('Quantity')
plt.ylabel('Total Order Amount')
plt.tight_layout()
plt.show()

# Pie Chart: Distribution of Order Types
order_type_counts = df['Order Type'].value_counts()
plt.figure(figsize=(8, 8))
order_type_counts.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("Set3", n_colors=len(order_type_counts)), fontsize=7,startangle=90)
plt.title('Distribution of Order Types')
plt.ylabel('')  # Hide the y-axis label
plt.tight_layout()
plt.show()

# Box Plot: Total Order Amount Distribution by Order Type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Order Type', y='Total', palette='Set2')
plt.title('Total Order Amount Distribution by Order Type')
plt.xlabel('Order Type')
plt.ylabel('Total Order Amount')
plt.tight_layout()
plt.show()      

print ("hoiiiii")

print("nan magand yekkada")
