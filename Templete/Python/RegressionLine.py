# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# %%
df = pd.read_csv(r'Data Visualization/scatter_plot_ii.csv')
df.head()
# %%
# There are two method in seaborn: regplot and lmplot <- Linear model
## first : regplot
plt.figure(figsize=(12,6), dpi = 300)
sns.set_style('white')
plt.xlabel('Ad Expenditure in (000\'s $)')
plt.ylabel('Sale in (000\'s $)')
plt.title('Effect of Ad Exp. on Sales', fontsize=14, fontweight='bold')
sns.regplot(x = 'Budget', y = 'Sales', data = df,
scatter_kws = {'color' : 'k'}, line_kws= {'color' : 'red'})
sns.despine(); # color : 同時改變marker and line, scatter_kws : 調整marker顏色, line_kws :調整line的顏色;
# %%
## Second : lmplot
### lmplot supports a wider range of features, so depending on your needs
### might be a more suitable option
plt.figure(dpi = 500)
sns.set_style('white')
sns.lmplot(x = 'Budget', y = 'Sales', data = df,
height = 10,
scatter_kws = {'color' : 'k'},
line_kws= {'color' : 'red'})
plt.xlabel('Ad Expenditure in (000\'s $)')
plt.ylabel('Sale in (000\'s $)')
plt.title('Effect of Ad Exp. on Sales', fontsize=14, fontweight='bold')
sns.despine();
