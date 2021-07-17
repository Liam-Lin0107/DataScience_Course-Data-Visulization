# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# use to turn axis into percentage
from matplotlib.ticker import PercentFormatter
sns.set()

# %%
df = pd.read_csv(r'/Users/lindazhong/Documents/Data_science_365/Data Visualization/bar_line_chart_data.csv')
df

# %%
sns.set_style('white')
# note : it's subplots not subplot
# ax : y-axis and x-axis
fig, ax = plt.subplots(figsize = (10, 7), dpi=500)
ax.bar(df.Year, df.Participants, color = 'k')
ax.set_ylabel('Number of Participants', fontweight = 'bold')
ax.tick_params(axis = 'y')
# use the same x-axis
ax1 = ax.twinx()

# setting the percentage ticker
ax1.set_ylim(0,1)
ax1.yaxis.set_major_formatter(PercentFormatter(xmax = 1.0))
###########

ax1.plot(df.Year, df["Python Users"], color = "#b60000", marker = "D")
ax1.set_ylabel('Python User in %', fontweight = 'bold')
ax.set_title('KD Nuggets Survey Python Users (2012-2019)', fontsize = 14, fontweight = 'bold');
