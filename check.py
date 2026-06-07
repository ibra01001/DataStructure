A = [1,2,3,4]
B = [2,3,4,5]

def check(A, B):

    while A and B:
        if A[0] == B[0]:
            A.pop(0)
            B.pop(0)
            return check(A, B)
        else:
            return False
    return False
print(check(A, B))