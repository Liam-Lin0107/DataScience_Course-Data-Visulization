# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %%
df_real_estate = pd.read_csv(r'/Users/lindazhong/Documents/Data science 365/Data Visualization/histogram_data.csv')
df_real_estate
# %%
sns.set_style('white')
plt.figure(figsize=(10,6),dpi = 300)
plt.hist(df_real_estate.Price, bins = 8, color='#108a99')
plt.title('Distribution of Real Estate Prices', fontsize=15, fontweight='bold')
plt.xlabel('Price in (000\' $)')
plt.ylabel('Number of Properties')
sns.despine();
