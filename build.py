import random

"""
example: 15*15
            1   1   2   2   3   1   
            2   1   2   1   1   2
            1   1   3   3   3   1
            1   1       1       3
            2   4               1
                1               2 ...
7,6         [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
4.3.4       [0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
1,2,2,2     [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
1,4,2,1     [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1]
1,3,1,2     [1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1]
1,1,2,3     [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0]
2,2,1,1,1,1 [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
1,1,1,3     [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0]
1,1         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
2,2,1,2,2   [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
1,1,1,1,1   [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
1,6,2       [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]
3,1,3,2     [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1]
1,1,2,1,3   [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]
3,1,3       [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]
"""
# # 构建主体矩阵
def build_matrix():
    mat = []
    for row in range(15):
        rowlist = []
        for i in range(15):
            rowlist.append(random.randint(0, 1))
        mat.append(rowlist)
    return mat
    # # 显示矩阵
    # for row in mat:
    #     print(row)

def row_index(mat):
    # 计算每行系数
    row_block = []
    for row in mat:
        row = row + [0, 0]
        l = 0
        block = []
        while row[l] == 0:
            l += 1
            # r+=1
        r = l + 1
        while (r < 15 + 1):
            if row[l] == 1 and row[r] == 1:
                r += 1
            elif row[l] == 1 and row[r] == 0:
                block.append(r - l)
                l = r + 1
                while (l < 15 + 2 and row[l] == 0):
                    l += 1
                r = l + 1
        row_block.append(block)
    return row_block

def column_index(mat):
    # 计算列系数
    column_block = []
    for i in range(15):
        column = []
        for j in range(15):
            column.append(mat[j][i])
        # columns.append(column_i)
        column = column + [0, 0]
        l = 0
        block = []
        while column[l] == 0:
            l += 1
            # r+=1
        r = l + 1
        while (r < 15 + 1):
            if column[l] == 1 and column[r] == 1:
                r += 1
            elif column[l] == 1 and column[r] == 0:
                block.append(r - l)
                l = r + 1
                while (l < 15 + 2 and column[l] == 0):
                    l += 1
                r = l + 1
        column_block.append(block)
    return column_block

def print_matrix(mat):
    print('—'*19)
    for row in mat:
        print('|'+' '.join([str(col) for col in row])+'|')
    print('—'*19)