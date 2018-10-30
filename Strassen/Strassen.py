###
# By: Oscar Vanderhorst
# Date: 09/27/18
# Purpose: Implementation for Strassen's algorithm on a static 4x4 matrix
#   Does not include recursion for the sake of this assignment.
###

X = [[2,2,2,1],[5,8,3,2],[3,3,5,9],[1,3,4,2]]
Y = [[5,4,2,1],[7,1,4,4],[4,8,6,3],[5,7,4,2]]

print("\nX Matrix : \t\tY Matrix: ")
print(str(X[0]) + "\t\t" + str(Y[0]));print(str(X[1]) + "\t\t" + str(Y[1]));
print(str(X[2]) + "\t\t" + str(Y[2]));print(str(X[3]) + "\t\t" + str(Y[3]));

#Because we have a static matrix, we do not use recursion on this function
#This is SIMPLY to show how the Strassen's algorithm would work on a broken down matrix
#Breaking it into 7 pieces instead of 8.
def strassMult(X, Y):
    #-- Separate them into 2x2
    #X
    A = [[X[0][0],X[0][1]],[X[1][0],X[1][1]]]
    print("\nA Submatrix: ")
    print(A[0]);print(A[1]);
    B = [[X[0][2],X[0][3]],[X[1][2],X[1][3]]]
    print("\nB Submatrix: ")
    print(B[0]);print(B[1]);
    C = [[X[2][0],X[2][1]],[X[3][0],X[3][1]]]
    print("\nC Submatrix: ")
    print(C[0]);print(C[1]);
    D = [[X[2][2],X[2][3]],[X[3][2],X[3][3]]]
    print("\nD Submatrix: ")
    print(D[0]);print(D[1]);

    #Y
    E = [[Y[0][0],Y[0][1]],[Y[1][0],Y[1][1]]]
    print("\nE Submatrix: ")
    print(E[0]);print(E[1]);
    F = [[Y[0][2],Y[0][3]],[Y[1][2],Y[1][3]]]
    print("\nF Submatrix: ")
    print(F[0]);print(F[1]);
    G = [[Y[2][0],Y[2][1]],[Y[3][0],Y[3][1]]]
    print("\nG Submatrix: ")
    print(G[0]);print(G[1]);
    H = [[Y[2][2],Y[2][3]],[Y[3][2],Y[3][3]]]
    print("\nH Submatrix: ")
    print(H[0]);print(H[1]);

    #Start getting the 7 partitions of Strassen's algorithm

    #P1 : A * (F - H)
    P_1 = matrixMult(A, matrixSub(F, H))
    print("\n----- P1 : A * (F - H)")
    print(P_1[0]);print(P_1[1]);
    #P2 : (A + B) * H
    P_2 = matrixMult(matrixAdd(A, B), H)
    print("\n----- P2 : (A + B) * H")
    print(P_2[0]);print(P_2[1]);
    #P3 : (C + D) * E
    P_3 = matrixMult(matrixAdd(C, D), E)
    print("\n----- P3 : (C + D) * E")
    print(P_3[0]);print(P_3[1]);
    #P4 : D * (G - E)
    P_4 = matrixMult(D, matrixSub(G, E))
    print("\n----- P4 : D * (G - E)")
    print(P_4[0]);print(P_4[1]);
    #P5 : (A + D) * (E + H)
    P_5 = matrixMult(matrixAdd(A, D), matrixAdd(E, H))
    print("\n----- P5 : (A + D) * (E + H)")
    print(P_5[0]);print(P_5[1]);
    #P6 : (B - D) * (G + H)
    P_6 = matrixMult(matrixSub(B, D), matrixAdd(G, H))
    print("\n----- P6 : (B - D) * (G + H)")
    print(P_6[0]);print(P_6[1]);
    #P7 : (A - C) * (E + F)
    P_7 = matrixMult(matrixSub(A, C), matrixAdd(E, F))
    print("\n----- P7 : (A - C) * (E + F)")
    print(P_7[0]);print(P_7[1]);

    #Getting the final matrix Z
    print("\n------- Final Matrix pieces: -------")

    #Z00 : P5 + P4 - P2 + P6
    Z_00 = matrixAdd(P_5, P_4)
    Z_00 = matrixSub(Z_00, P_2)
    Z_00 = matrixAdd(Z_00, P_6)
    print("\n----- Z00 : P5 + P4 - P2 + P6")
    print(Z_00[0]);print(Z_00[1]);
    #Z01 : P1 + P2
    Z_01 = matrixAdd(P_1, P_2)
    print("\n----- Z01 : P1 + P2")
    print(Z_01[0]);print(Z_01[1]);
    #Z10 : P3 + P4
    Z_10 = matrixAdd(P_3, P_4)
    print("\n----- Z10 : P3 + P4")
    print(Z_10[0]);print(Z_10[1]);
    #Z11 : P1 + P5 - P3 - P7
    Z_11 = matrixAdd(P_1, P_5)
    Z_11 = matrixSub(Z_11, P_3)
    Z_11 = matrixSub(Z_11, P_7)
    print("\n----- Z11 : P1 + P5 - P3 - P7")
    print(Z_11[0]);print(Z_11[1]);

    print("\n\n-----Final Matrix: \n")
    print(Z_00[0] + Z_01[0])
    print(Z_00[1] + Z_01[1])
    print(Z_10[0] + Z_11[0])
    print(Z_10[1] + Z_11[1])


#Addition of len 2 matrices
def matrixAdd(X, Y):
    Z = [[0,0],[0,0]]
    for i in range(0, 2):
        for j in range(0, 2):
            Z[i][j] = X[i][j] + Y[i][j]
    
    return Z

#Subraction of len 2 matrices
def matrixSub(X, Y):
    Z = [[0,0],[0,0]]
    for i in range(0, 2):
        for j in range(0, 2):
            Z[i][j] = X[i][j] - Y[i][j]
    
    return Z

#Multiplication of len 2 matrices
def matrixMult(X, Y):
    Z = [[0,0],[0,0]]
    for i in range(0, 2):
        for k in range(0, 2):
            for j in range(0, 2):
                Z[i][j] += X[i][k] * Y[k][j]
    
    return Z


strassMult(X, Y)