import twint
import pandas as pd 
hn = pd.read_csv("hanoi.csv")
user = hn['username'].values
for i in range(0,len(user)):
    c = twint.Config()
    c.Username = user[i]
    c.Store_csv = True
    c.Output = "data2.csv"
    c.Custom["user"] = ["location"]
    c.Hide_output = True
    twint.run.Lookup(c)
