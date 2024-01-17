# Program to add two matrices using nested loop


X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# for row in range(len(X)):
#     for column in range(len(X[0])):
#         result[row][column] = X[row][column] + Y[row][column]


result = [[X[row][column] + Y[row][column] for column in range(len(X[0])) ]for row in range(len(X))]
for r in result:
    print(r)