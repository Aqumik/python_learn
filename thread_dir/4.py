

# 加权算法

list1 = [6.3,6.19,11.62,4.0,9.3]
list2 = []
resu = round(6.3 / sum(list1),2)

print(sum(list1))
print(resu)

for i in range(len(list1)):
    avr = round(list1[i] / sum(list1),2)
    list2.append(round(avr * 500))


print(list2)
print(sum(list2))