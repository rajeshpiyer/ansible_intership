# %%
import pandas as pd



# %%
dataset = pd.read_excel("ip_v4.xlsx")


# %%
x = dataset['IPV4']


# %%
y = dataset['STREAM']


# %%
file1 = open("inventory","w")

file1.write("[data_science]\n")
count = len(x)
for i in range(0,count):
  if y[i]=="data_science":
    file1.write(str(x[i])+"\n")

file1.write("[networking]\n")
for i in range(0,count):
  if y[i]=="networking":
    file1.write(str(x[i])+"\n")

file1.write("[mca:children]\ndata_science\nnetworking")

file1.close()


