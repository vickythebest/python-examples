items1=[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
def diagonal_sum(given_3d):
    total=0
    for i in range(len(given_3d)):
        total+=given_3d[i][i]
    return total

# print(diagonal_sum(items1))

#You're given a configuration of a chessboard with some rooks. 
# In this chessboard, we want to see if any of the rooks are able to attack any other ones. 
# Just in case you've never played chess, rooks are able to move any number of spaces horizontally and vertically
items=[[0,1,0,0],
       [0,0,0,1],
       [0,0,1,0],
       [0,0,1,0]]

# def rooks_are_safe(input):
#     n=len(input)
#     for row_i in range(n):
#         row_count=0
#         for col_i in range(n):
#             row_count+=input[row_i][col_i]
#         print("--row_count--",row_count)
#         if row_count > 1:
#             return False
#     for col_i in range(n):
#         col_count=0
#         for row_i in range(n):
#             col_count+=input[row_i][col_i]
#         print("--col_count--",col_count)
#         if col_count > 1:
#             return False
#     return True

def rooks_are_safe(input):
    n=len(input)
    for j in range(n):
        row_count=0
        for i in range(n):
            row_count+=input[i][j]
        print("--row_count--",row_count)
        if row_count > 1:
            return False
    for i in range(n):
        col_count=0
        for j in range(n):
            col_count+=input[j][i]
        print("--col_count--",col_count)
        if col_count > 1:
            return False
    return True



print(rooks_are_safe(items))