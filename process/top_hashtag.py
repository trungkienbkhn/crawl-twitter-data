import pandas as pd 
hn = pd.read_csv("hanoi1.csv")
a = hn['username'].values
b = hn['name'].values
c = hn['hashtags'].values
d = hn['tweet'].values
list_ht = []
print("Tweets: ",len(c))
for i in range(0,len(c)):
    if (c[i] != "[]"):
        e = c[i].split("', '")
        e[0] = e[0].lstrip("['")
        e[len(e)-1] = e[len(e)-1].rstrip("']")
        for j in range(0,len(e)):
            list_ht.append(e[j])

dem = 0
while (dem<21):  
    max = 0
    j = 0
    for i in range(0,len(list_ht)):
        if (max < list_ht.count(list_ht[i])):
            max = list_ht.count(list_ht[i])
            top = list_ht[i]
    print(top,"~",max)
    while (list_ht.count(top) > 0):
        if (list_ht[j] == top):
            list_ht.pop(j)
            j -= 1
        j += 1

    dem += 1


#hashtag = pd.DataFrame()
#hashtag['username'] = a
#hashtag['name'] = b
#hashtag['hashtags'] = c
#hashtag['tweet'] = d
#hashtag.to_csv("hashtag.csv")
