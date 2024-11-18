my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x=0
y=0
while len(my_list) > x:
    if my_list[y] >= 0:
        print(my_list[y])
        x +=1
        y +=1
    else:
        break
