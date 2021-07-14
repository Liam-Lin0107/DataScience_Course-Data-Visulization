# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %%
# loading date
df = pd.read_csv(r"Data Visualization/scatter_data.csv")
df.head()


# %%
# plotting
plt.figure(dpi = 500, figsize=(12,8))
# alpha : transparency, c : hue in sns, cmap : the third dimension colors
## in order to show the legend, we need to save it into a variable
### 'mako' and 'viridis' are good
scatter = plt.scatter(df["Area (ft.)"], df["Price"],
alpha = 0.6, c = df["Building Type"], cmap = 'viridis')
# * : c++ pointer to the legend element to the scatter
plt.legend(*scatter.legend_elements(), loc = 'upper left', title = 'Building Type')
plt.title('Relationship between Area and Price in California', fontsize=14, fontweight='bold');
plt.xlabel('Area in (sq. ft.)')
plt.ylabel('Price in (000\'s of $)');

# %%
# using seaborn to plot
plt.figure(dpi = 500, figsize=(12,8))
# s : size of marker, alpha : transparency, palette = camp in matplotlib
sns.scatterplot(x = df["Area (ft.)"],y = df["Price"], hue = df["Building Type"],
palette='mako',s = 100, alpha = 0.6)
plt.title('Relationship between Area and Price in California', fontsize=14, fontweight='bold');
plt.xlabel('Area in (sq. ft.)')
plt.ylabel('Price in (000\'s of $)');
