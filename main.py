data=input()
data=data.replace("[","")
data=data.replace("]","")
data=data.replace(" ","")
list=data.split(",")
print(data)
list1=[]
for i in list:
    if i.isnumeric():
        list1.append(int(i))
    else:
        i=i.replace("'","")
        i=i.replace("\"","")
        liste1.append(i)
print(list1)
