a=input()
A=[]
B=[]
for i in a:
    A.append(i)
B=A[::-1]
if A==B:
    print(True)
else:
    print(False)