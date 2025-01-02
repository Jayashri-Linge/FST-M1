list1 = [12,23,34,10]
list2 = [2,3,4,5,6]

print("first List : " , list1)
print("Second List : " , list2)

resultList = []

for ele in list1:
    if(ele % 2 != 0):
        resultList.append(ele)

for ele in list2:
    if(ele % 2 ==0):
        resultList.append(ele)

print("The result List is: " ,resultList)