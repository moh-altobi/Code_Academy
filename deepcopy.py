import copy
x=[[[1, 2, 3],[4, 5, 6]],[[1, 2, 3],[4, 5, 6]]]
y=copy.deepcopy(x)
y[0][0][0]=100
y[0][1][2]=50
y[1][1][2]=500


print(x)
print(y)
