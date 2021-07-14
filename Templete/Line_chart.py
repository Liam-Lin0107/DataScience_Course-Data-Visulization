# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %%
df_spx_ftse = pd.read_csv(r'/Users/lindazhong/Documents/Data_science_365/Data Visualization/line_chart_data.csv')
df_spx_ftse
# tranfer date from string into date
df_spx_ftse["new_date"] = pd.to_datetime(df_spx_ftse.Date)
df_spx_ftse

# %%
plt.figure(figsize=(20,5), dpi = 300)
plt.title('S&P 500 vs. FTSE Returns (2000-2010)', fontsize=14, fontweight='bold')
plt.ylabel('Returns')
plt.xlabel('Date')
plt.plot(df_spx_ftse.new_date, df_spx_ftse.GSPC500, label='S&P 500')
plt.plot(df_spx_ftse.new_date, df_spx_ftse.FTSE100, label = 'FTSE 100')
plt.legend(loc = 'upper left', fontsize='large');
# %%
# slicing the Data
df_spx_ftse_H2_08 = df_spx_ftse[(df_spx_ftse.new_date>='2008-07-01') & (df_spx_ftse.new_date<='2008-12-31')]

sns.set_palette('rocket')
ax = plt.figure(figsize=(20,5), dpi =400)
plt.title('S&P 500 vs. FTSE Returns (2000-2010)', fontsize=14, fontweight='bold')
plt.ylabel('Returns')
plt.xlabel('Date')
plt.plot(df_spx_ftse_H2_08.new_date, df_spx_ftse_H2_08.GSPC500, label='S&P 500')
plt.plot(df_spx_ftse_H2_08.new_date,df_spx_ftse_H2_08.FTSE100, label = 'FTSE 100')
plt.legend(loc = 'upper left', fontsize='large')
plt.savefig('S&P 500 vs. FTSE Returns (2000-2010).png', dpi = 500);
# %%
# 用pandas 畫畫看
df = df_spx_ftse_H2_08.iloc[:,[2,1]]
df.index = df_spx_ftse_H2_08.iloc[:,3].values
df
ax = df.plot()
# 設定y軸百分比
from matplotlib.ticker import FuncFormatter
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2%}'.format(y)))
