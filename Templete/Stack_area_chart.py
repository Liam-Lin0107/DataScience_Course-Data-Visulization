# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %%
df = pd.read_csv(r'/Users/lindazhong/Documents/Data_science_365/Data Visualization/stack-area-chart.csv')
df.head()
# %%
labels = df.columns.values[1:4]
labels = labels[-1]
sns.set_palette('rocket')
sns.set_style('white')
plt.figure(figsize=(11,5),dpi = 300)
plt.stackplot(df.Year, df.Diesel, df.Petrol, df.Gas,
edgecolor = 'none', labels = labels),
plt.xticks(df.Year.values, rotation = 90)
plt.title('The Popularity of Car Engine over Time', fontsize=15, fontweight='bold')
sns.despine();
