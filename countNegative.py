items=[[-4,-3,-1,0],
       [-2,-2, 1,2],
       [-1, 1, 2,3],
       [1,  2, 4,5]]

def countNegative(list):
    count=0
    row_i=0
    col_i=len(list) - 1
    while col_i >= 0 and row_i < len(list):
        if list[row_i][col_i] < 0:
            count += (col_i+1)
            row_i += 1
        else:
            col_i -= 1
    return count

print(countNegative(items))
