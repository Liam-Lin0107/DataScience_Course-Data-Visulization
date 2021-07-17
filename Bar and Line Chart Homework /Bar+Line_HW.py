# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter
sns.set()

# %%
df = pd.read_csv(r'bar_line_chart_homework.csv')
df
# %%
sns.set_style('white')
fig, ax = plt.subplots(figsize=(12,8), dpi =500)
ax.bar(x = df["Movie Theater Goers Complaints"], height = df["Number of complaints"], color = 'k')
ax.set_ylabel('Number of Complaints', fontsize = 9)

ax1 = ax.twinx()
ax1.set_ylim(0,1.1)
ax1.yaxis.set_major_formatter(PercentFormatter(xmax=1))
ax1.plot(df["Movie Theater Goers Complaints"], df.frequency, color = '#b60000', marker = 'D')
ax1.set_ylabel("Frequency", fontsize = 9)
ax1.set_title("Top 5 Movie Geor Complaints Frequency", fontsize = 14, fontweight = 'bold');
