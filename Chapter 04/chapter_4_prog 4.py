import numpy as np
#A: Coefficient Matrix
A=[[2,5,2],[3,-2,4],[-6,1,-7]]
A=np.array(A)
#print(type(A))
print(A)
#B: Constant Matrix based on Solution
b=[[-38],[17],[-12]]
b=np.array(b)
#print(type(B))
print(b)
detA=np.linalg.det(A)
if detA==0:
    print("Solution is not possible!")
else:
    InvA = np.linalg.inv(A)
    C= np.matmul(InvA,b)
    print("Solution: x = {}, y= {}, z={}".format(C[[0]],C[[1]],C[[2]]))