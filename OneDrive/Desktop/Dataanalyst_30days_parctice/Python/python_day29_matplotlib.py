#!/usr/bin/env python
# coding: utf-8

# In[1]:


#day29_matplotlib_basics 

import matplotlib.pyplot as plt

# Sample data
products = ["Laptop", "Phone", "Tablet", "Headphones"]
sales = [150, 300, 120, 90]

# Create a bar chart
plt.figure(figsize=(6,4))
plt.bar(products, sales, color="skyblue")

# Add labels and title
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.title("Sales by Product")

# Show grid and plot
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()


# In[ ]:




