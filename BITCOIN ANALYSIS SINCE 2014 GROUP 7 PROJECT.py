#!/usr/bin/env python
# coding: utf-8

# # BITCOIN ANALYSIS SINCE 2014
# ![bitcon.jpg](attachment:bitcon.jpg)
# 
# 

# In[6]:


pwd


# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


BTC = pd.read_csv("BTC-USD.csv")
print(BTC.shape)
BTC.head(20)


# ![Candle%20sticks.jpg](attachment:Candle%20sticks.jpg)
# Basic info

# In[11]:


BTC.describe()


# **The mean, average and std dev of the value of bitcoin over the past 9 years.**
# **The higest and the lowest value of bitcoin overtime.**
# 
# The highest value of bitcoin= 68789.625000
# The lowest value of bitcoin= 171.509995
# The starndard deviation= 16015.763332
# The mean = 13672.568197

# In[20]:


BTC.groupby('Date')['Close'].mean()


# In[29]:


BTC.isnull().sum()


# In[31]:


# Line plot of Bitcoin price over time
plt.figure(figsize=(12, 6))
plt.plot(BTC['Date'], BTC['Close'])
plt.xlabel('Date')
plt.ylabel('Bitcoin Price')
plt.title('Bitcoin Price Over Time')
plt.xticks(rotation=45)
plt.show()

# Histogram of Bitcoin price distribution
plt.figure(figsize=(8, 6))
sb.histplot(BTC['Close'], bins=30)
plt.xlabel('Bitcoin Price')
plt.ylabel('Frequency')
plt.title('Bitcoin Price Distribution')
plt.show()


# **The posible trend, is the price going up or down?**
# **The period with highest highs**
# The trend of the bitcon price first steadily rises but in the year 2019 and 2020 there was a sharp rise to the highest value in the year 2020. 
# Then a continual drop is noted for the following years till the end of 2022 but in this year there has been a pull in both sides but tentatively rising.

# **Which are the most common prices?**
# On the second bar graph it shows the prices mainly have a domain mainly on the lower prices below the 10000 mark and very rarely above 60000

# In[35]:


correlation_matrix = BTC.corr()
plt.figure(figsize=(10, 8))
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

plt.scatter(BTC['High'], BTC['Low'])
plt.xlabel('High')
plt.ylabel('Low')
plt.title('Scatter Plot: High vs. Low')
plt.show()


# **The corelation of volume to the highs and lows**
# The Corelation Heatmap shows that the high and low are fully correlated.
# The scatter map shows they are more correlated in the lower values than the higher values as they tend to scatter
