# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df_fuel_engine_type = pd.read_csv('/Users/lindazhong/Documents/Data science 365/Data Visualization/pie chart.csv')
df_fuel_engine_type



# %%
sns.set()
sns.set_palette('colorblind')
plt.figure(figsize=(10,8), dpi = 100)
plt.pie(df_fuel_engine_type['Number of Cars'], labels=df_fuel_engine_type['Engine Fuel Type'].values, autopct = '%.2f%%',
textprops={'size':'x-large', 'fontweight':'bold','rotation':'30', 'color':'w'},explode=[0.009]*4)
plt.legend()
plt.title('Cars by Engine Fuel Type', fontsize=18, fontweight='bold');
