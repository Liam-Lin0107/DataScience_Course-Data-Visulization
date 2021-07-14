# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df_used_cars = pd.read_csv(r'/Users/lindazhong/Documents/Data science 365/Data Visualization/car_brand.csv')
df_used_cars
# %%
sns.set()
plt.figure(dpi = 150)
plt.barh(y = df_used_cars["Brand"], width = df_used_cars["Cars Listings"], color= "y")
plt.title("Car Listins by Brand", fontsize = 16, fontweight="bold")
plt.xlabel("Number of Listins", fontsize = 13, fontweight="bold"),
plt.yticks(fontsize=9);
