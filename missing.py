string=input()
list1=[]
for i in string[::]:
    if i not in list1:
        list1.append(i)
print(len(list1))
