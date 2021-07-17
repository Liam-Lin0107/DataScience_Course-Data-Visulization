# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# %%
df_stock_ret = pd.read_csv(r'Data Visualization/Line Chart Homework /returns1020.csv')
df_stock_ret
# %%
df_stock_ret["new_date"] = pd.to_datetime(df_stock_ret.Date)
df_stock_ret
# %%
sns.set_palette('rocket')
plt.figure(dpi = 500)
sns.set_style('white')
df_stock_ret_slice = df_stock_ret[(df_stock_ret.new_date >= "2011-05-01") &(df_stock_ret.new_date <= "2012-6-30")]
plt.plot(df_stock_ret_slice.new_date, df_stock_ret_slice.GSPCRet)
plt.plot(df_stock_ret_slice.new_date, df_stock_ret_slice.FTSERet)
plt.title("GSPCRet vs. FTSERet from 2011-05 to 2012-06", fontsize=13, fontweight = 'bold')
sns.despine();
