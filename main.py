veri=input()
veri=veri.replace("[","")
veri=veri.replace("]","")
liste=veri.split(",")
print(veri)
liste1=[]
for i in liste:
    if i.isnumeric():
        liste1.append(int(i))
    else:
        i=i.replace("'","")
        i=i.replace("\"","")
        liste1.append(i)
print(liste1)
