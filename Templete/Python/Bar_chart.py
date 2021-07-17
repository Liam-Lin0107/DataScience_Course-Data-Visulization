# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
df_used_cars = pd.read_csv(r'/Users/lindazhong/Documents/Data science 365/Data Visualization/car_brand.csv')
df_used_cars
# %%
sns.set()
plt.figure(figsize=(9,6),dpi=100)
plt.title("Cars Listings by Brand", fontweight= "bold", fontsize= 16)
plt.ylabel("Number of Listings", fontsize = 13)
plt.bar(x = df_used_cars["Brand"], height = df_used_cars["Cars Listings"],color = ["r","g","b","w","y","m","c"])
plt.xticks(rotation= 45, fontsize=13)
plt.yticks(fontsize=13)
plt.savefig("Use Cars Bar.png");
# %%
sns.set()
plt.figure(figsize=(9,6), dpi = 100)
plt.bar(x = df_used_cars["Brand"], height = df_used_cars["Cars Listings"], color= "midnightblue")
plt.xticks(rotation = 45,fontsize=13)
plt.yticks(fontsize=13)
plt.title("Car Listings by Brand", fontsize=16, fontweight="bold")
plt.ylabel("Number of Listings",size=13);
