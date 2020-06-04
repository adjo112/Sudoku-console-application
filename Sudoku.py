matrix = [
    [5,0,0,4,0,0,0,2,0],
    [6,0,0,0,7,5,0,0,0],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [3,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [0,2,0,0,0,7,4,0,0],
    [0,4,0,2,0,6,0,0,0]
]


def cal(mat):
    find = nextemptyspot(mat)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(mat, i, (row, col)):
            mat[row][col] = i

            if cal(mat):
                return True

            mat[row][col] = 0

    return False


def valid(mat, num, pos):
  
    for i in range(len(mat[0])):
        if mat[pos[0]][i] == num and pos[1] != i:
            return False

   
    for i in range(len(mat)):
        if mat[i][pos[1]] == num and pos[0] != i:
            return False

    
    matx_x = pos[1] // 3
    matx_y = pos[0] // 3

    for i in range(matx_y*3, matx_y*3 + 3):
        for j in range(matx_x * 3, matx_x*3 + 3):
            if mat[i][j] == num and (i,j) != pos:
                return False

    return True


def print_matrix(mat):
    for i in range(len(mat)):
        if i % 3 == 0 and i != 0:
            print("**************************")

        for j in range(len(mat[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(mat[i][j])
            else:
                print(str(mat[i][j]) + " ", end="")


def nextemptyspot(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return (i, j)

    return None

print_matrix(matrix)
solve(matrix)
print_matrix(matrix)
