# %%
import pandas as pd



# %%
dataset = pd.read_csv("ip_v4.csv")


# %%
x = dataset['IPV4']


# %%
y = dataset['STREAM']
a = dataset['USERNAME']
b = dataset['PASSWORD']


# %%
file1 = open("inventory","w")

file1.write("[data_science]\n")
count = len(x)
for i in range(0,count):
  if y[i]=="data_science":
    file1.write(str(x[i])+" ansible_user="+str(a[i])+" ansible_ssh_pass="+str(b[i])+"\n")

file1.write("[networking]\n")
for i in range(0,count):
  if y[i]=="networking":
    file1.write(str(x[i])+" ansible_user="+str(a[i])+" ansible_ssh_pass="+str(b[i])+"\n")

file1.write("[mca:children]\ndata_science\nnetworking")

file1.close()



