ml = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(
    *[i for i in ml if ml.count(i) == 1]
)