# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()
# %%
df = pd.read_csv(r'student_scores_data.csv')
df
# %%
plt.figure(dpi =300, figsize=(10,7))
sns.set_style('white')
plt.scatter(x = df.SAT, y = df.GPA, alpha =0, c = 'midnightblue')
plt.title('SAT Scores vs. GAP Scores', fontsize=14, fontweight='bold')
plt.xlabel('SAT Scores', fontsize=9)
plt.ylabel('GAP Scores', fontsize=9)
sns.despine();
