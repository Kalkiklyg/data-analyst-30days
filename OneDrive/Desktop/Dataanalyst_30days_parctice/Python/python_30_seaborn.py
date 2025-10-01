#!/usr/bin/env python
# coding: utf-8

# In[1]:


#day30_seaborn_basics
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset (Seaborn has built-in ones)
df = sns.load_dataset("tips")  # restaurant tips dataset

# 1. Inspect data
print(df.head())

# 2. Histogram of total bill amounts
plt.figure(figsize=(6,4))
sns.histplot(df['total_bill'], kde=True, color="skyblue")
plt.title("Distribution of Total Bills")
plt.show()

# 3. Scatterplot of total bill vs tip, colored by gender
plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df, palette="Set1")
plt.title("Tips vs Total Bill by Gender")
plt.show()

# 4. Boxplot of total bill across days
plt.figure(figsize=(6,4))
sns.boxplot(x="day", y="total_bill", data=df, palette="Set2")
plt.title("Total Bill Distribution per Day")
plt.show()


# In[ ]:




