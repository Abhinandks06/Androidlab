import numpy as np


m=np.array([[5,6,4],[2,5,6],[3,5,6]])
U,S,VT=np.linalg.svd(m)
print(f"U :{U}")
print(f"S :{np.diag(S)}")
print(f"VT :{VT}")
n=np.dot(U, np.dot(np.diag(S), VT))
print(f"Reconstructed matrix {n}")