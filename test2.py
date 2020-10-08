name = "ethan!"
name2 = "jones"
name3 = name+" "+name2
print(name3)


#bubble sort
list1 = [5,1,18,6,7,20,19,31]
something = 0
while True:
    for i in range(0,len(list1)-1):
        if list1[i]>list1[i+1]:
            temp1=list1[i]
            temp2 = list1[i+1]
            list1[i] = temp2
            list1[i+1] = temp1
            something = 1
    if something== 0:
        break
    something = 0
print(list1)


