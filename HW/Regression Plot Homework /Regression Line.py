# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# %%
df = pd.read_csv(r'regression_auto_insurance_sweden.csv')
df


# %%
## sns regplot
sns.set_style('white')
plt.figure(figsize=(10,6),dpi=300)
sns.regplot(x = 'Claims', y = 'Payment', data = df,
scatter_kws = {'color' : 'k'}, line_kws= {'color' : 'red'})
plt.title('Relationship between Claims and Payment', fontsize=14, fontweight='bold')
sns.despine();
# %%
## lmplot
sns.set_style('white')
plt.figure(dpi=1000)
sns.lmplot(x = 'Claims', y = 'Payment', data = df,
scatter_kws = {'color' : 'k'}, line_kws= {'color' : 'red'})
plt.title('Relationship between Claims and Payment', fontsize=14, fontweight='bold')
sns.despine();
