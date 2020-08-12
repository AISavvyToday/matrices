import numpy as np
while True:
    op = input('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit: ''')
    if op == '0':
        break
    elif op == '1':
        A_dims = input("Enter size of first matrix: ").split()
        A_rows = int(A_dims[0])
        A_cols = int(A_dims[1])
        A = [input("Enter first matrix: ").split() for i in range(A_rows)]

        B_dims = input("Enter size of second matrix: ").split()
        B_rows = int(B_dims[0])
        B_cols = int(B_dims[1])
        B = [input("Enter second matrix: ").split() for i in range(B_rows)]
        results = []
        if A_rows == B_rows and A_cols == B_cols:
            for i in range(A_rows):
                for j in range(A_cols):
                    a = float(A[i][j])
                    b = float(B[i][j])
                    c = a + b
                    results.append(c)
            for i in [results[c:c+A_cols] for c in range(0,len(results),A_cols) if c%A_cols == 0]:
                print("The result is:")
                print(*i)
        else:
            print("The operation cannot be performed.")
    elif op == '2':
        dims = input("Enter size of first matrix: ").split()
        rows = int(dims[0])
        cols = int(dims[1])
        matrix = [input("Enter matrix: ").split() for i in range(rows)]
        scalar = float(input())
        results = []
        for inner in matrix:
            for j in inner:
                k = float(j) * scalar
                results.append(k)
        for i in [results[c:c+cols] for c in range(0,len(results),cols) if c%cols == 0]:
            print("The result is:")
            print(*i)
    elif op == '3':
        A_dims = input("Enter size of first matrix: ").split()
        A_rows = int(A_dims[0])
        A_cols = int(A_dims[1])
        A = [input("Enter first matrix: ").split() for i in range(A_rows)]
        B_dims = input("Enter size of second matrix: ").split()
        B_rows = int(B_dims[0])
        B_cols = int(B_dims[1])
        B = [input("Enter second matrix: ").split() for i in range(B_rows)]
        if A_cols == B_rows:
            results = [[0 for col in range(B_cols)] for row in range(A_rows)]
            for i in range(A_rows):
                for j in range(B_cols):
                    for k in range(B_rows):
                        results[i][j] += float(A[i][k]) * float(B[k][j])
            for i in results:
                print("The result is:")
                print(*i)
        else:
            print("The operation cannot be performed.")
    elif op == '4':
        t_type = input('''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line: ''')
        if t_type == '1':
            dims = input("Enter size of first matrix: ").split()
            rows = int(dims[0])
            cols = int(dims[1])
            matrix = [input("Enter matrix: ").split() for i in range(rows)]
            new_matrix = [[0 for i in range(rows)] for j in range(cols)]
            for i in range(rows):
                for j in range(cols):
                    new_matrix[i][j] = matrix[j][i]
            for i in new_matrix:
                print("The result is:")
                print(*i)
        elif t_type == '2':
            dims = input("Enter size of first matrix: ").split()
            rows = int(dims[0])
            cols = int(dims[1])
            matrix = [input("Enter matrix: ").split() for i in range(rows)]
            new_matrix = [[0 for i in range(rows)] for j in range(cols)]
            results = []
            for i in reversed(range(rows)):
                for j in reversed(range(cols)):
                    results.append(matrix[j][i])
            for i in [results[c:c+cols] for c in range(0,len(results),cols) if c%cols == 0]:
                print("The result is:")
                print(*i)
        elif t_type == '3':
            dims = input("Enter size of first matrix: ").split()
            rows = int(dims[0])
            cols = int(dims[1])
            matrix = [input("Enter matrix: ").split() for i in range(rows)]
            results = []
            for i in range(rows):
                for j in reversed(range(cols)):
                    results.append(matrix[i][j])
            for i in [results[c:c+cols] for c in range(0,len(results),cols) if c%cols == 0]:
                print("The result is:")
                print(*i)
        elif t_type == '4':
            dims = input("Enter size of first matrix: ").split()
            rows = int(dims[0])
            cols = int(dims[1])
            matrix = [input("Enter matrix: ").split() for i in range(rows)]
            print(matrix)
            results = []
            for i in reversed(range(rows)):
                for j in range(cols):
                    results.append(matrix[i][j])
            for i in [results[c:c+cols] for c in range(0,len(results),cols) if c%cols == 0]:
                print("The result is:")
                print(*i)
    elif op == '5':
        dims = input("Enter size of first matrix: ").split()
        rows = int(dims[0])
        cols = int(dims[1])
        matrix = [[int(i) if i.isdigit() else float(i) for i in input().split()] for i in range(rows)]
        print(matrix)
        if rows == cols:
            det = np.linalg.det(matrix)
            print("The result is: \n{}".format(det))
        else:
            print("The operation cannot be performed.")
    elif op == '6':
        dims = input("Enter size of first matrix: ").split()
        rows = int(dims[0])
        cols = int(dims[1])
        matrix = [[int(i) if i.isdigit() else float(i) for i in input().split()] for i in range(rows)]
        det = np.linalg.det(matrix)

        if det == 0:
            print("This matrix doesn't have an inverse.")
        else:
            inverse = np.linalg.inv(matrix)
            for i in inverse:
                print("The result is:")
                print(*i)
