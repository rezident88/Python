#Напишите программу для печати всех уникальных значений в словаре.
#Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_1=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
list1=[]
for i in list_1:
    for value in i.values():
        list1.append(value)
print(set(list1))
