# %%
import pandas as pd



# %%
dataset = pd.read_csv("user_passwords.csv")


# %%
x = dataset['USERNAME']

# %%
y = dataset['PASSWORD']

# %%
file1 = open("user_passwords.yml","w")

file1.write("user_passwords:\n")
count = len(x)
for i in range(0,count):
  file1.write("\t"+str(x[i])+":"+str(y[i])+"\n")
file1.close()



