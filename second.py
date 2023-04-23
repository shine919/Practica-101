list1 = [1,4,6]
list2 = [11,33,22]
a = list(set(list2))
a.sort()
res = []
for i in a:
    for j in range(0, len(list2)):
        if(list2[j] == i):
            res.append(list1[j])
print(res)