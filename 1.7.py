grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
print(students)
x=0
q=0
a=[]
d=[]
for i in grades:
    if x<6:
        while x<6:
            l=sum(grades[x])/len(grades[x])
            a.append(l)
            d.append(students[q])
            q+=1
            x+=1
            r = zip(d, a)
            print(dict(r))
    else:
        break


