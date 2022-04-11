def s(z):
    for i in range(len(z)-1):
        print(z[i],i)
        for j in range(i):
            if z[j]>z[j+1]:
                z[j],z[j+1]=z[j+1],z[j]
    return z


z=[54,26,93,17,77,31,44,55,1123123]
print(s(z))
## 1213